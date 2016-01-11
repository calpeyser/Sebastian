import sebastian.src.SebastianStructures.Constants as Constants
from ParallelIntervalError import ParallelIntervalError
from ParallelIntervalCheck import ParallelIntervalCheck

from music21.interval import Interval

class ParallelOctaveCheck(ParallelIntervalCheck):

    def create_error(self, part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2):
        return ParallelOctaveError(part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2)

    def illegal_interval_list(self):
        return [Interval(12)]

class ParallelOctaveError(ParallelIntervalError):

    def __init__(self, part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2):
        super(self.__class__, self).__init__("Octave", part_number_1, part_number_2, measure_and_beat_1, measure_and_beat_2)

    def get_error_name(self):
        return "ParallelOctaveError"