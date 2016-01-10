from sebastian.src.SebastianStructures.ChoraleEvaluation import ChoraleError
import sebastian.src.SebastianStructures.Constants as Constants


class ParallelIntervalError(ChoraleError):

    def __init__(self, interval_name, part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2):
        message = "Parallel %s between %s and %s. First unison at measure %s beat %s. Second unison at measure %s beat %s." % \
                       (interval_name, Constants.PART_NAMES[part_number_1], Constants.PART_NAMES[part_number_2], measure_and_beat_1[0], measure_and_beat_1[1], measure_and_beat_2[0], measure_and_beat_2[1])

        self.interval_name = interval_name
        self.part_number_1 = part_number_1
        self.part_number_2 = part_number_2
        self.measure_and_beat_1 = measure_and_beat_1
        self.measure_and_beat_2 = measure_and_beat_2

        super(ParallelIntervalError, self).__init__(message)

    def get_interval_name(self):
        return self.interval_name

    def get_part_number_1(self):
        return self.part_number_1

    def get_part_number_2(self):
        return self.part_number_2

    def get_measure_1(self):
        return self.measure_and_beat_1[0]

    def get_beat_1(self):
        return self.measure_and_beat_1[1]

    def get_measure_2(self):
        return self.measure_and_beat_2[0]

    def get_beat_2(self):
        return self.measure_and_beat_2[1]