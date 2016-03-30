from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import XMLChoraleAnalysis
import sebastian.tests.testfiles.TestFilePaths as TestFilePaths
from sebastian.src.SebastianStructures import Constants
from sebastian.src.Utils.Utils import *

import unittest


class TritoneJumpIntegrationTests(unittest.TestCase):
    def test_ThrowsErrorWithTritoneJump(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.tritone_jump)
        analysis.analyze()
        errors = analysis.get_error_list("TritoneJumpError")
        self.assertEqual(3, len(errors))


    def test_ErrorHasCorrectProperties(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.tritone_jump)
        analysis.analyze()
        errors = analysis.get_error_list("TritoneJumpError")
        self.assertEqual(1.0, errors[0].get_measure_1())
        self.assertEqual(1.0, errors[0].get_measure_2())
        self.assertEqual(0.0, errors[0].get_beat_1())
        self.assertEqual(1.0, errors[0].get_beat_2())

if __name__ == "__main__":
    unittest.main()
