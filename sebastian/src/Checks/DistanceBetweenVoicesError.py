from sebastian.src.SebastianStructures.ChoraleEvaluation import ChoraleError
import sebastian.src.SebastianStructures.Constants as Constants


class DistanceBetweenVoicesError(ChoraleError):

    def __init__(self, high_pitch, low_pitch, high_part, low_part, measure_and_beat, notes):
        message = "The interval between %s in %s and %s in %s, at measure %s beat %s, is greater than an octave." % \
                       (high_pitch, Constants.PART_NAMES[high_part], low_pitch, Constants.PART_NAMES[low_part], measure_and_beat.measure, measure_and_beat.beat)

        self.high_part = high_part
        self.low_part = low_part
        self.measure_and_beat = measure_and_beat
        self.high_pitch = high_pitch
        self.low_pitch = low_pitch
        self.notes = notes
        s = 'high part = ' + Constants.PART_NAMES[high_part]
        print(s)
        super(DistanceBetweenVoicesError, self).__init__(message, self.notes)

    def get_high_pitch(self):
        return self.high_pitch

    def get_low_pitch(self):
        return self.low_pitch

    def get_high_part(self):
        return self.high_part

    def get_low_part(self):
        return self.low_part

    def get_measure(self):
        return self.measure_and_beat.measure

    def get_beat(self):
        return self.measure_and_beat.beat

    def get_error_name(self):
        return "DistanceBetweenVoicesError"