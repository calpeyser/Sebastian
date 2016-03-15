import sebastian.src.Utils.Utils as Utils
import sebastian.src.SebastianStructures.Check as Check
import sebastian.src.SebastianStructures.Constants as Constants
from sebastian.src.Checks.Location import Location
from sebastian.src.Checks.TritoneJumpError import TritoneJumpError

class TritoneJumpCheck(Check):
    def run_check(self, chorale):
        out = []
        #TODO
        '''
        get offset list for all parts (note: offsets)
        get a reverse map
        get pitchspace (pitch.ps) for notes in sequence, make sure they are not +3

        '''

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

        index = 0
        while index < 4:
            previous_offset = offset_lists[index][0]
            previous_note = reverse_note_maps[index][previous_offset]
            for offset in offset_lists[index][1:]:
                current_note = reverse_note_maps[index][offset]
                current_pitch = current_note.pitch
                previous_pitch = previous_note.pitch
                if current_pitch.ps - previous_pitch.ps == 3.0:
                    current_location = chorale.get_location_from_offset(offset)
                    previous_location = chorale.get_location_from_offset(previous_offset)
                    part = Constants.PART_NAMES[index]
                    error = TritoneJumpError(part, previous_pitch, previous_location, current_pitch, current_location)
                    out.append(error)
                previous_note = current_note
                previous_offset = offset
            index = index + 1
        return out

