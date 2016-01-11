import sebastian.src.SebastianStructures.Check as Check
import sebastian.src.SebastianStructures.Constants as Constants

from music21.interval import Interval

class ParallelIntervalCheck(Check):

    def run_check(self, chorale):
        out = []
        out.extend(self.run_check_for_parts(chorale, Constants.ALTO_PART_NUMBER, Constants.TENOR_PART_NUMBER))

        return out


    def run_check_for_parts(self, chorale, part_number_1, part_number_2):
        offsets = chorale.get_offset_list(part_number_1)

        # for each note in part1, will check if lines up in unison to part2.  If so, will check next note.
        out = []
        for index, offset in enumerate(offsets[:-1]):
            if chorale.get_interval_between_parts_at_offset(part_number_1, part_number_2, offset) in self.illegal_interval_list():
                if chorale.get_interval_between_parts_at_offset(part_number_1, part_number_2, offsets[index + 1]) in self.illegal_interval_list():
                    out.append(self.create_error(part_number_1, part_number_2, chorale.get_measure_and_beat_from_offset(offset), chorale.get_measure_and_beat_from_offset(offsets[index + 1])))
        return out

    def create_error(self, part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2):
        pass

    def illegal_interval_list(self):
        pass