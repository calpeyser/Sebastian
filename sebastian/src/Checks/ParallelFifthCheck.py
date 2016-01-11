import sebastian.src.SebastianStructures.Constants as Constants
from ParallelIntervalError import ParallelIntervalError
from ParallelIntervalCheck import ParallelIntervalCheck

from music21.interval import Interval

class ParallelFifthCheck(ParallelIntervalCheck):

    def create_error(self, part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2):
        return ParallelFifthError(part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2)

    def illegal_interval_list(self):
        return [Interval(6), Interval(7)]

class ParallelFifthError(ParallelIntervalError):

    def __init__(self, part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2):
        super(self.__class__, self).__init__("Fifth", part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2)

    def get_error_name(self):
        return "ParallelFifthError"