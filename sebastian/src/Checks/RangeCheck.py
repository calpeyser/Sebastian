import sebastian.src.Utils.Utils as Utils
import sebastian.src.SebastianStructures.Check as Check
import sebastian.src.SebastianStructures.Constants as Constants
from sebastian.src.Checks.Location import Location
from sebastian.src.Checks.RangeError import RangeError
from sebastian.src.Checks.Range import Range


class RangeCheck(Check):
    def run_check(self, chorale):
        out = []
        ranges = [
            self.set_range('SOPRANO_PART_NUMBER'),
            self.set_range('ALTO_PART_NUMBER'),
            self.set_range('TENOR_PART_NUMBER'),
            self.set_range('BASS_PART_NUMBER')
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
                note = reverse_note_maps[i][offset].nameWithOctave
                value = self.convert_note_to_value(note)
                if value > ranges[i].max or value < ranges[i].min:
                    location = chorale.get_location_from_offset(offset)
                    error = RangeError(note, Constants.PART_NAMES[i], location)
                    out.append(error)
            i += 1

        return out

    def set_range(self, part):
        min = None
        max = None
        if part == 'SOPRANO_PART_NUMBER':
            min = self.convert_note_to_value('C4')
            max = self.convert_note_to_value('G5')
        if part == 'ALTO_PART_NUMBER':
            min = self.convert_note_to_value('G3')
            max = self.convert_note_to_value('D5')
        if part == 'TENOR_PART_NUMBER':
            min = self.convert_note_to_value('C3')
            max = self.convert_note_to_value('G4')
        if part == 'BASS_PART_NUMBER':
            min = self.convert_note_to_value('F2')
            max = self.convert_note_to_value('C4')

        return Range(min, max)

    def convert_note_to_value(self, note):
        note_values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}
        split_note = list(note)
        pitch = split_note[0]
        value = note_values[pitch]
        value += split_note[1]
        return value
