import sebastian.src.Utils.Utils as Utils
import sebastian.src.SebastianStructures.Check as Check
import sebastian.src.SebastianStructures.Constants as Constants
from sebastian.src.Checks.Location import Location
from sebastian.src.Checks.RangeError import RangeError
from sebastian.src.Checks.Range import Range

import music21.note as note


# def run_check(self, chorale):
#         out = []
#         out.extend(self.run_check_for_parts(chorale, Constants.TENOR_PART_NUMBER, Constants.ALTO_PART_NUMBER))
#         out.extend(self.run_check_for_parts(chorale, Constants.ALTO_PART_NUMBER, Constants.SOPRANO_PART_NUMBER))
#         return out
#
#     def run_check_for_parts(self, chorale, part_1, part_2):
#         out = []
#         notes_for_part = chorale.reverse_note_maps
#         for offset in notes_for_part[part_1]:
#             #check if offset exists in notes_for_part[part_2]
#             if offset in notes_for_part[part_2]:
#                 pitch_1 = notes_for_part[part_1][offset].pitch
#                 pitch_2 = notes_for_part[part_2][offset].pitch
#                 if pitch_2.ps - pitch_1.ps > 12.0:
#                     error = DistanceBetweenVoicesError(pitch_1, pitch_2, part_1, part_2, chorale.get_location_from_offset(offset))
#                     out.append(error)
#         return out




class RangeCheck(Check):
    def run_check(self, chorale):
        out = []
        out.extend(self.check_part(Constants.SOPRANO_PART_NUMBER, chorale.get_range_for_part(Constants.SOPRANO_PART_NUMBER), chorale))
        out.extend(self.check_part(Constants.ALTO_PART_NUMBER, chorale.get_range_for_part(Constants.ALTO_PART_NUMBER), chorale))
        out.extend(self.check_part(Constants.TENOR_PART_NUMBER, chorale.get_range_for_part(Constants.TENOR_PART_NUMBER), chorale))
        out.extend(self.check_part(Constants.BASS_PART_NUMBER, chorale.get_range_for_part(Constants.BASS_PART_NUMBER), chorale))
        return out

    def check_part(self, part, range, chorale):
        out = []
        for note, offset in chorale.note_maps[part].items():
            pitch = note.pitch
            offset = note.offset
            if pitch > range.max or pitch < range.min:
                location = chorale.get_location_from_offset(offset)
                error = RangeError(pitch, Constants.PART_NAMES[part], location)
                out.append(error)
        return out

'''
a note is not a unique key value so necessary to access notes via a reverse_note_map,
which maps notes to offsets, in order to keep track of the notes location. It's a good idea
to create an object which wraps the music_21 note and holds a location attribute.

'''


