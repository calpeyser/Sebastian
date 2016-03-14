from sebastian.src.SebastianStructures.ChoraleEvaluation import ChoraleError
import sebastian.src.SebastianStructures.Constants as Constants
import sebastian.src.Checks.Location as Location


class RangeError(ChoraleError):
    def __init__(self, pitch, part, location):
        message = 'the note %s is out of range in the %s at measure %s beat %s' % (
        pitch, part, location.get_measure(), location.get_beat())
        self.location = location
        self.pitch = pitch
        self.part = part
        super(RangeError, self).__init__(message)

    def get_error_name(self):
        return "RangeError"

    def get_pitch(self):
        return self.pitch

    def get_measure(self):
        return self.location.get_measure()

    def get_beat(self):
        return self.location.get_beat()
