import sebastian.src.Utils.Utils as Utils
import sebastian.src.SebastianStructures.Check as Check
import sebastian.src.SebastianStructures.Constants as Constants
from sebastian.src.Checks.Location import Location
from sebastian.src.Checks.RangeError import RangeError
from sebastian.src.Checks.Range import Range

import music21.note as note

class RangeCheck(Check):
    def run_check(self, chorale):
        out = []
        ranges = [
            self.set_range(0),
            self.set_range(1),
            self.set_range(2),
            self.set_range(3)
        ]

        offset_lists = [
            chorale.get_offset_list(Constants.SOPRANO_PART_NUMBER),
            chorale.get_offset_list(Constants.ALTO_PART_NUMBER),
            chorale.get_offset_list(Constants.TENOR_PART_NUMBER),
            chorale.get_offset_list(Constants.BASS_PART_NUMBER)
        ]

        reverse_note_maps = [
            chorale.get_reverse_note_map(Constants.SOPRANO_PART_NUMBER),
            chorale.get_reverse_note_map(Constants.ALTO_PART_NUMBER),
            chorale.get_reverse_note_map(Constants.TENOR_PART_NUMBER),
            chorale.get_reverse_note_map(Constants.BASS_PART_NUMBER)
        ]

        i = 0
        while i < 4:
            for offset in offset_lists[i]:
                note = reverse_note_maps[i][offset]
                pitch = Utils.get_only_element(note.pitches)
                if pitch > ranges[i].max or pitch < ranges[i].min:
                    location = chorale.get_location_from_offset(offset)
                    error = RangeError(note, Constants.PART_NAMES[i], location)
                    out.append(error)
            i += 1

        return out

    def set_range(self, part):
        if part == 0:
            min = note.Note('C4')
            max = note.Note('G5')
        if part == 1:
            min = note.Note('G3')
            max = note.Note('D5')
        if part == 2:
            min = note.Note('C3')
            max = note.Note('G4')
        if part == 3:
            min = note.Note('F2')
            max = note.Note('C4')

        return Range(min, max)