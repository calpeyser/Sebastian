from sebastian.src.SebastianStructures.ChoraleEvaluation import ChoraleError
import sebastian.src.SebastianStructures.Constants as Constants


class AdjacentPartsGreaterThanOctaveError(ChoraleError):

    def __init__(self, pitch_1, pitch_2, part_number_1, part_number_2, measure_and_beat):
        message = "The interval between %s in %s and %s in %s, at measure %s beat %s, is greater than an octave." % \
                       (pitch_1, Constants.PART_NAMES[part_number_1], pitch_2, Constants.PART_NAMES[part_number_2], measure_and_beat.measure, measure_and_beat.beat)

        self.part_number_1 = part_number_1
        self.part_number_2 = part_number_2
        self.measure_and_beat = measure_and_beat
        self.pitch_1 = pitch_1
        self.pitch_2 = pitch_2
        super(AdjacentPartsGreaterThanOctaveError, self).__init__(message)

        print message

    def get_part_number_1(self):
        return self.part_number_1

    def get_part_number_2(self):
        return self.part_number_2

    def get_measure(self):
        return self.measure_and_beat[0]

    def get_beat(self):
        return self.measure_and_beat[1]

    def get_error_name(self):
        return "AdjacentPartsGreaterThanOctaveError"