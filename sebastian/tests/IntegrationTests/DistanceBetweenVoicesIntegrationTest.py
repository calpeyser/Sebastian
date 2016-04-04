from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import XMLChoraleAnalysis
import sebastian.tests.testfiles.TestFilePaths as TestFilePaths
from sebastian.src.SebastianStructures import Constants
from sebastian.src.Utils.Utils import *

import unittest

class DistanceBetweenVoicesIntegrationTest(unittest.TestCase):

    def test_ThrowsErrorWithBadDistanceBetweenVoices(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.bad_distance_between_voices)
        analysis.analyze()
        errors = analysis.get_error_list("DistanceBetweenVoicesError")
        self.assertEqual(1, len(errors))

    def test_CorrectPropertiesOnDistanceBetweenVoices(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.bad_distance_between_voices)
        analysis.analyze()
        error = get_only_element(analysis.get_error_list("DistanceBetweenVoicesError"))
        self.assertEqual(14, error.get_high_pitch().ps - error.get_low_pitch().ps)
        self.assertEqual(Constants.ALTO_PART_NUMBER, error.get_low_part())
        self.assertEqual(Constants.SOPRANO_PART_NUMBER, error.get_high_part())
        self.assertEqual(2, error.get_measure())
        self.assertEqual(0.0, error.get_beat())

if __name__ == "__main__":
    unittest.main()