from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import XMLChoraleAnalysis
import sebastian.tests.testfiles.TestFilePaths as TestFilePaths
from sebastian.src.SebastianStructures import Constants
from sebastian.src.Utils.Utils import *

import unittest


class RepBassIntegrationTests(unittest.TestCase):
    def test_ThrowsErrorWithRepBass(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.rep_bass)
        analysis.analyze()
        errors = analysis.get_error_list("RepBassError")
        self.assertEqual(1, len(errors))

    def test_ErrorHasCorrectProperties(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.rep_bass)
        analysis.analyze()
        error = get_only_element(analysis.get_error_list("RepBassError"))
        self.assertEqual(3.0, error.get_measure_1())
        self.assertEqual(3.0, error.get_measure_2())
        self.assertEqual(0.0, error.get_beat_1())
        self.assertEqual(1.0, error.get_beat_2())


if __name__ == "__main__":
    unittest.main()
