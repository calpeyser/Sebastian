from sebastian.src.SebastianStructures.ChoraleEvaluation import ChoraleError
import sebastian.src.SebastianStructures.Constants as Constants


class RepBassError(ChoraleError):
    def __init__(self, measure_1, measure_2, pitch):
        message = "repeated %s in bass at measures %s and %s ."(pitch, measure_1, measure_2)

        self.pitch = pitch
        self.measure_1 = measure_1
        self.measure_2 = measure_2

        super(RepBassError, self).__init__(message)

    def get_error_name(self):
        return "RepBassError"

    def get_pitch(self):
        return self.pitch

    def get_measure_1(self):
        return self.measure_1

    def get_measure_2(self):
        return self.measure_2
