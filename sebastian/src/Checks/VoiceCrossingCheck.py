import sebastian.src.Utils.Utils as Utils
import sebastian.src.SebastianStructures.Check as Check
import sebastian.src.SebastianStructures.Constants as Constants
from sebastian.src.Checks.Location import Location
from sebastian.src.Checks.VoiceCrossingError import VoiceCrossingError


class VoiceCrossingCheck(Check):
    def run_check(self, chorale):
        out = []
        out.extend(self.run_check_for_parts(chorale, Constants.BASS_PART_NUMBER, Constants.TENOR_PART_NUMBER))
        out.extend(self.run_check_for_parts(chorale, Constants.TENOR_PART_NUMBER, Constants.ALTO_PART_NUMBER))
        out.extend(self.run_check_for_parts(chorale, Constants.ALTO_PART_NUMBER, Constants.SOPRANO_PART_NUMBER))
        return out

    def run_check_for_parts(self, chorale, part_1, part_2):
        out = []
        for offset in chorale.reverse_note_maps[part_1]:
            #check if offset exists in notes_for_part[part_2]
            if offset in chorale.reverse_note_maps[part_2]:
                pitch_1 = chorale.reverse_note_maps[part_1][offset].pitch
                pitch_2 = chorale.reverse_note_maps[part_2][offset].pitch
                notes = [chorale.reverse_note_maps[part_1][offset], chorale.reverse_note_maps[part_2][offset]]

                if pitch_1.ps > pitch_2.ps:
                    error = VoiceCrossingError(pitch_1, pitch_2, part_1, part_2, chorale.get_location_from_offset(offset), notes)
                    out.append(error)
        return out
