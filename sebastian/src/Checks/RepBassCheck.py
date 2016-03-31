import sebastian.src.Utils.Utils as Utils
import sebastian.src.SebastianStructures.Check as Check
import sebastian.src.SebastianStructures.Constants as Constants
from sebastian.src.Checks.Location import Location
from sebastian.src.Checks.RepBassError import RepBassError


class RepBassCheck(Check):
    def run_check(self, chorale):
        out = []
        offset_list = chorale.get_offset_list(Constants.BASS_PART_NUMBER)
        reverse_note_map = chorale.get_reverse_note_map(Constants.BASS_PART_NUMBER)

        previous_offset = offset_list[0]
        previous_note = reverse_note_map[previous_offset]
        previous_pitch = previous_note.pitch
        for offset in offset_list[1:]:
            current_note = reverse_note_map[offset]
            current_pitch = current_note.pitch
            previous_pitch = previous_note.pitch
            if current_pitch == previous_pitch:
                current_location = chorale.get_location_from_offset(offset)
                previous_location = chorale.get_location_from_offset(previous_offset)
                error = RepBassError(current_pitch, previous_location, current_location, [previous_note, current_note])
                out.append(error)
            previous_note = current_note
            previous_offset = offset
        return out
