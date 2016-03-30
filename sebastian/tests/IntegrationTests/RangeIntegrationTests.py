from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import XMLChoraleAnalysis
import sebastian.tests.testfiles.TestFilePaths as TestFilePaths
from sebastian.src.SebastianStructures import Constants
from music21.pitch import Pitch
from sebastian.src.Utils.Utils import *

import unittest


class RangeIntegrationTests(unittest.TestCase):
    def test_ThrowsErrorWithRange(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.out_of_range)
        analysis.analyze()
        errors = analysis.get_error_list('RangeError')
        self.assertEqual(1, len(errors))

    def test_ErrorHasCorrectProperties(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.out_of_range)
        analysis.analyze()
        error = get_only_element(analysis.get_error_list("RangeError"))
        self.assertEqual(1.0, error.get_measure())
        self.assertEqual('soprano', error.get_part())
        expected_pitch = Pitch('B3')
        self.assertEqual(expected_pitch, error.get_pitch())

if __name__ == "__main__":
    unittest.main()
