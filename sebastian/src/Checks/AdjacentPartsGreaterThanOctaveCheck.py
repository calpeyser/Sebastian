import sebastian.src.Utils.Utils as Utils
import sebastian.src.SebastianStructures.Check as Check
import sebastian.src.SebastianStructures.Constants as Constants
from sebastian.src.Checks.Location import Location
from sebastian.src.Checks.AdjacentPartsGreaterThanOctaveError import AdjacentPartsGreaterThanOctaveError


class AdjacentPartsGreaterThanOctaveCheck(Check):
    def run_check(self, chorale):
        out = []
        out.extend(self.run_check_for_parts(chorale, Constants.TENOR_PART_NUMBER, Constants.ALTO_PART_NUMBER))
        out.extend(self.run_check_for_parts(chorale, Constants.ALTO_PART_NUMBER, Constants.SOPRANO_PART_NUMBER))
        return out

    def run_check_for_parts(self, chorale, part_1, part_2):
        out = []
        notes_for_part = chorale.reverse_note_maps
        for offset in notes_for_part[part_1]:
            #check if offset exists in notes_for_part[part_2]
            if offset in notes_for_part[part_2]:
                pitch_1 = notes_for_part[part_1][offset].pitch
                pitch_2 = notes_for_part[part_2][offset].pitch
                if pitch_2.ps - pitch_1.ps > 12.0:
                    error = AdjacentPartsGreaterThanOctaveError(pitch_1, pitch_2, part_1, part_2, chorale.get_location_from_offset(offset))
                    out.append(error)
        return out
