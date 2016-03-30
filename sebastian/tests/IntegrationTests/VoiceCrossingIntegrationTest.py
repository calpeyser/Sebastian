from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import XMLChoraleAnalysis
import sebastian.tests.testfiles.TestFilePaths as TestFilePaths
from sebastian.src.SebastianStructures import Constants
from sebastian.src.Utils.Utils import *

import unittest


class VoiceCrossingIntegrationTests(unittest.TestCase):
    def test_ThrowsErrorWithVoiceCrossing(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.voice_crossing)
        analysis.analyze()
        errors = analysis.get_error_list("VoiceCrossingError")
        self.assertEqual(2, len(errors))


    # def test_ErrorHasCorrectProperties(self):
    #     analysis = XMLChoraleAnalysis(TestFilePaths.voice_crossing)
    #     analysis.analyze()
    #     error = get_only_element(analysis.get_error_list("VoiceCrossingError"))
    #     self.assertEqual(1.0, error.get_measure())
    #     self.assertEqual(0.0, error.get_beat())


if __name__ == "__main__":
    unittest.main()
