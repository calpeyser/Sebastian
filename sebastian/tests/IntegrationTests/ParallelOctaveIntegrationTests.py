from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import XMLChoraleAnalysis
import sebastian.tests.testfiles.TestFilePaths as TestFilePaths
from sebastian.src.SebastianStructures import Constants
from sebastian.src.Utils.Utils import *

import unittest

class ParallelOctaveIntegrationTests(unittest.TestCase):

    def test_ThrowsErrorWithParallelOctaves(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.parallel_octave)
        analysis.analyze()
        errors = analysis.get_error_list("ParallelOctaveError")
        for error in errors:
            print error.message
        self.assertEqual(1, len(errors))

    def test_CorrectPropertiesOnParallelOctaveError(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.parallel_octave)
        analysis.analyze()
        error = get_only_element(analysis.get_error_list("ParallelOctaveError"))

        self.assertEqual("Octave", error.get_interval_name())
        self.assertEqual(Constants.ALTO_PART_NUMBER, error.get_part_number_1())
        self.assertEqual(Constants.TENOR_PART_NUMBER, error.get_part_number_2())
        self.assertEqual(2, error.get_measure_1())
        self.assertEqual(1.0, error.get_beat_1())
        self.assertEqual(2, error.get_measure_2())
        self.assertEqual(2.0, error.get_beat_2())

if __name__ == "__main__":
    unittest.main()