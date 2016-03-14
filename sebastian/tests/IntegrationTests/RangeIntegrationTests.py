from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import XMLChoraleAnalysis
import sebastian.tests.testfiles.TestFilePaths as TestFilePaths
from sebastian.src.SebastianStructures import Constants
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


if __name__ == "__main__":
    unittest.main()
