from sebastian.src.SebastianStructures.ChoraleEvaluation import ChoraleError
import sebastian.src.Checks.Location as Location

class TritoneJumpError(ChoraleError):
    def __init__(self, part, pitch_1, location_1, pitch_2, location_2):
        message = "tritone jump (%s - %s) in %s at measure %s beat %s and measure %s beat %s" % (
        pitch_1, pitch_2, part, location_1.get_measure(), location_1.get_beat(), location_2.get_measure(), location_2.get_beat())
        self.pitch_1 = pitch_1
        self.pitch_2 = pitch_2
        self.location_1 = location_1
        self.location_2 = location_2
        super(TritoneJumpError, self).__init__(message)

    def get_error_name(self):
        return "TritoneJumpError"

    def get_pitch_1(self):
        return self.pitch_1

    def get_pitch_2(self):
        return self.pitch_2

    def get_measure_1(self):
        return self.location_1.get_measure()

    def get_beat_1(self):
        return self.location_1.get_beat()

    def get_measure_2(self):
        return self.location_2.get_measure()

    def get_beat_2(self):
        return self.location_2.get_beat()