import sebastian.src.Utils.Utils as Utils
import sebastian.src.SebastianStructures.Check as Check
import sebastian.src.SebastianStructures.Constants as Constants
from sebastian.src.Checks.Location import Location
from sebastian.src.Checks.DistanceBetweenVoicesError import DistanceBetweenVoicesError


class DistanceBetweenVoicesCheck(Check):
    def run_check(self, chorale):
        out = []
        out.extend(self.run_check_for_parts(chorale, Constants.TENOR_PART_NUMBER, Constants.ALTO_PART_NUMBER))
        out.extend(self.run_check_for_parts(chorale, Constants.ALTO_PART_NUMBER, Constants.SOPRANO_PART_NUMBER))
        return out

    def run_check_for_parts(self, chorale, low_part, high_part):
        out = []
        notes_for_part = chorale.reverse_note_maps
        for offset in notes_for_part[high_part]:
            #check if offset exists in notes_for_part[part_2]
            if offset in notes_for_part[low_part]:
                high_note = notes_for_part[high_part][offset]
                low_note = notes_for_part[low_part][offset]
                if high_note.pitch.ps - low_note.pitch.ps > 12.0:
                    notes = [high_note, low_note]
                    error = DistanceBetweenVoicesError(high_note.pitch, low_note.pitch, high_part, low_part, chorale.get_location_from_offset(offset), notes)
                    out.append(error)
        return out