from sebastian.src.SebastianStructures.ChoraleEvaluation import ChoraleError
import sebastian.src.Checks.Location as Location


class RepBassError(ChoraleError):
    def __init__(self, pitch, location_1, location_2, notes):
        message = "repeated %s in bass at measure %s beat %s and measure %s beat %s" % (
        pitch, location_1.get_measure(), location_1.get_beat(), location_2.get_measure(), location_2.get_beat())
        self.pitch = pitch
        self.location_1 = location_1
        self.location_2 = location_2
        self.notes = notes
        super(RepBassError, self).__init__(message, self.notes)

    def get_error_name(self):
        return "RepBassError"

    def get_pitch(self):
        return self.pitch

    def get_measure_1(self):
        return self.location_1.get_measure()

    def get_beat_1(self):
        return self.location_1.get_beat()

    def get_measure_2(self):
        return self.location_2.get_measure()

    def get_beat_2(self):
        return self.location_2.get_beat()
