import sebastian.src.Utils.Utils as Utils
import sebastian.src.SebastianStructures.Check as Check
import sebastian.src.SebastianStructures.Constants as Constants
from sebastian.src.Checks.Location import Location
from sebastian.src.Checks.TritoneJumpError import TritoneJumpError

class TritoneJumpCheck(Check):
    def run_check(self, chorale):
        out = []

        out.extend(self.run_check_for_part(chorale, Constants.SOPRANO_PART_NUMBER))
        out.extend(self.run_check_for_part(chorale, Constants.ALTO_PART_NUMBER))
        out.extend(self.run_check_for_part(chorale, Constants.TENOR_PART_NUMBER))
        out.extend(self.run_check_for_part(chorale, Constants.BASS_PART_NUMBER))

        return out

    def run_check_for_part(self, chorale, part):
        out = []
        offsets = chorale.offset_lists[part]
        reverse_note_map = chorale.reverse_note_maps[part]
        previous_offset = offsets[0]
        previous_note = reverse_note_map[previous_offset]
        #part, pitch_1, location_1, pitch_2, location_2, notes
        for offset in offsets[1:]:
            current_note = reverse_note_map[offset]
            current_pitch = current_note.pitch
            previous_pitch = previous_note.pitch
            if current_pitch.ps - previous_pitch.ps == 3.0:
                current_location = chorale.get_location_from_offset(offset)
                previous_location = chorale.get_location_from_offset(previous_offset)
                error = TritoneJumpError(part, previous_pitch, previous_location, current_pitch, current_location, [previous_note, current_note])
                out.append(error)
            previous_note = current_note
            previous_offset = offset
        return out


