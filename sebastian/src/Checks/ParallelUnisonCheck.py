import sebastian.src.SebastianStructures.Constants as Constants
from ParallelIntervalError import ParallelIntervalError
from ParallelIntervalCheck import ParallelIntervalCheck

from music21.interval import Interval

class ParallelUnisonCheck(ParallelIntervalCheck):

    def create_error(self, part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2, notes):
        return ParallelUnisonError(part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2, notes)

    def illegal_interval_list(self):
        return [Interval(0)]

class ParallelUnisonError(ParallelIntervalError):

    def __init__(self, part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2, notes):
        super(self.__class__, self).__init__("Unison", part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2, notes)

    def get_error_name(self):
        return "ParallelUnisonError"