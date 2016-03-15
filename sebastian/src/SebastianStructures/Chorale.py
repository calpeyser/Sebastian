import Constants

from music21.stream import Score as Score
from music21.stream import Measure
from music21.note import Note
from music21.tie import Tie
from music21.interval import notesToChromatic
from sebastian.src.Checks.Location import Location


class Chorale():
    """
    A wrapper over a music21.stream.Score instance that represents the chorale under evaluation.
    """

    @staticmethod
    def fromScore(score):
        """
        Static constructor.

        :param score: A score, likely the result of a parsing.
        :return: A Chorale instance wrapping the score.
        """
        return Chorale(score)

    def __init__(self, score):
        self.score = score

        self.soprano = self.get_score().parts[Constants.SOPRANO_PART_NUMBER]
        self.alto = self.get_score().parts[Constants.ALTO_PART_NUMBER]
        self.tenor = self.get_score().parts[Constants.TENOR_PART_NUMBER]
        self.bass = self.get_score().parts[Constants.BASS_PART_NUMBER]

        self.parts = [
            self.soprano,
            self.alto,
            self.tenor,
            self.bass
        ]

        # maps notes -> offsets
        self.note_maps = [
            self._construct_note_map(Constants.SOPRANO_PART_NUMBER),
            self._construct_note_map(Constants.ALTO_PART_NUMBER),
            self._construct_note_map(Constants.TENOR_PART_NUMBER),
            self._construct_note_map(Constants.BASS_PART_NUMBER)
        ]

        self.note_lists = [
            self._construct_note_list(Constants.SOPRANO_PART_NUMBER),
            self._construct_note_list(Constants.ALTO_PART_NUMBER),
            self._construct_note_list(Constants.TENOR_PART_NUMBER),
            self._construct_note_list(Constants.BASS_PART_NUMBER),
        ]

        self.full_note_list = [
            self._construct_full_note_list(Constants.SOPRANO_PART_NUMBER),
            self._construct_full_note_list(Constants.ALTO_PART_NUMBER),
            self._construct_full_note_list(Constants.TENOR_PART_NUMBER),
            self._construct_full_note_list(Constants.BASS_PART_NUMBER),

        ]

        # maps offsets -> notes
        self.reverse_note_maps = [
            self._construct_reverse_note_map(Constants.SOPRANO_PART_NUMBER),
            self._construct_reverse_note_map(Constants.ALTO_PART_NUMBER),
            self._construct_reverse_note_map(Constants.TENOR_PART_NUMBER),
            self._construct_reverse_note_map(Constants.BASS_PART_NUMBER),
        ]

        self.offset_lists = [
            self._construct_offset_list(Constants.SOPRANO_PART_NUMBER),
            self._construct_offset_list(Constants.ALTO_PART_NUMBER),
            self._construct_offset_list(Constants.TENOR_PART_NUMBER),
            self._construct_offset_list(Constants.BASS_PART_NUMBER)
        ]


    def get_score(self):
        """
        :return: The score wrapped by this Chorale instance.
        """
        return self.score

    def get_note_map(self, part_number):
        return self.note_maps[part_number]

    def get_note_list(self, part_number):
        return self.note_lists[part_number]

    def get_reverse_note_map(self, part_number):
        return self.reverse_note_maps[part_number]

    # returns list of note and octave
    def get_full_note_list(self, part_number):
        return self.full_note_list[part_number]

    def get_offset_list(self, part_number):
        return self.offset_lists[part_number]

    def get_note_at_offset(self, part_number, target_offset):
        nearest_offset = self.get_offset_list(part_number)[0]
        for offset in self.get_offset_list(part_number):
            if offset <= target_offset:
                nearest_offset = offset
            else:
                break
        return self.get_reverse_note_map(part_number)[nearest_offset]

    def get_interval_between_parts_at_offset(self, part_number_1, part_number_2, offset):
        note_1 = self.get_note_at_offset(part_number_1, offset)
        note_2 = self.get_note_at_offset(part_number_2, offset)

        return notesToChromatic(note_1, note_2)

    def get_measure_and_beat_from_offset(self, offset):
        # ugly hack...
        measure_list = self._get_part_measures(Constants.SOPRANO_PART_NUMBER)
        for index, measure in enumerate(measure_list[:-1]):
            if measure.offset <= offset and measure_list[index + 1].offset > offset:
                return index + 1, offset - measure.offset
        else:
            last_measure = self._get_part_measures(Constants.SOPRANO_PART_NUMBER)[-1]
            return len(self._get_part_measures(Constants.SOPRANO_PART_NUMBER)), offset - last_measure.offset

    def get_location_from_offset(self, offset):
        measure_and_beat = self.get_measure_and_beat_from_offset(offset)
        return Location(measure_and_beat[0], measure_and_beat[1])

    def _get_part_measures(self, part_number):
        measures = [element for element in self.parts[part_number] if isinstance(element, Measure)]
        return sorted(measures, key = lambda m: m.offset)

    def _construct_note_map(self, part_number):
        out = {}
        for measure in self._get_part_measures(part_number):
            for element in measure:
                if (isinstance(element, Note)):
                    if not element.tie == Tie("stop"):
                        out[element] = measure.offset + element.offset
        return out

    def _construct_reverse_note_map(self, part_number):
        out = {}
        for measure in self._get_part_measures(part_number):
            for element in measure:
                if (isinstance(element, Note)):
                    if not element.tie == Tie("stop"):
                        out[measure.offset + element.offset] = element
        return out

    def _construct_note_list(self, part_number):
        out = []
        for measure in self._get_part_measures(part_number):
            for element in measure:
                if (isinstance(element, Note)):
                    if not element.tie == Tie("stop"):
                        out.append(element)
        return out

    def _construct_full_note_list(self, part_number):
        out = []
        note_list = self._construct_note_list(part_number)
        for note in note_list:
            out.append(note.nameWithOctave)
        return out

    def _construct_offset_list(self, part_number):
        out = []
        for measure in self._get_part_measures(part_number):
            for element in measure:
                if (isinstance(element, Note)):
                    if not element.tie == Tie("stop"):
                        out.append(measure.offset + element.offset)
        return out
