from sebastian.src.SebastianStructures.ChoraleEvaluation import ChoraleError
import sebastian.src.SebastianStructures.Constants as Constants


class VoiceCrossingError(ChoraleError):

    def __init__(self, pitch_1, pitch_2, part_number_1, part_number_2, measure_and_beat, notes):
        message = "%s in %s voice crosses %s in %s in measure %s, beat %s" % (pitch_1, Constants.PART_NAMES[part_number_1],pitch_2, Constants.PART_NAMES[part_number_2], measure_and_beat.measure, measure_and_beat.beat)
        self.pitch_1 = pitch_1
        self.pitch_2 = pitch_2
        self.part_number_1 = part_number_1
        self.part_number_2 = part_number_2
        self.measure_and_beat = measure_and_beat

        super(VoiceCrossingError, self).__init__(message, notes)

    def pitch_1(self):
        return self.pitch_1

    def pitch_2(self):
        return self.pitch_2

    def get_part_number_1(self):
        return self.part_number_1

    def get_part_number_2(self):
        return self.part_number_2

    def get_measure(self):
        return self.measure_and_beat.measure

    def get_beat(self):
        return self.measure_and_beat.beat

    def get_error_name(self):
        return "VoiceCrossingError"