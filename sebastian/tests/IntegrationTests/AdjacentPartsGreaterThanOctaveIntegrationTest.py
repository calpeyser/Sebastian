from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import XMLChoraleAnalysis
import sebastian.tests.testfiles.TestFilePaths as TestFilePaths
from sebastian.src.SebastianStructures import Constants
from sebastian.src.Utils.Utils import *

import unittest

class AdjacentPartsGreaterThanOctaveIntegrationTest(unittest.TestCase):

    def test_ThrowsErrorWithAdjacentsGreaterThanOvtave(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.adjacents_greater_than_octave)
        analysis.analyze()
        errors = analysis.get_error_list("AdjacentPartsGreaterThanOctaveError")
        self.assertEqual(1, len(errors))

    def test_CorrectPropertiesOnAdjacentsGreaterThanOvtave(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.parallel_fifth)
        analysis.analyze()
        error = get_only_element(analysis.get_error_list("AdjacentPartsGreaterThanOctaveError"))

        self.assertEqual(14, error.get_pitch_1().ps - error.get_pitch_2().ps)
        self.assertEqual(Constants.ALTO_PART_NUMBER, error.get_part_number_1())
        self.assertEqual(Constants.SOPRANO_PART_NUMBER, error.get_part_number_2())
        self.assertEqual(2, error.get_measure())
        self.assertEqual(0.0, error.get_beat_1())

if __name__ == "__main__":
    unittest.main()