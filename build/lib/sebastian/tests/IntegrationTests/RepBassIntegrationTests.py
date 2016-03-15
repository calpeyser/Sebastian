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


if __name__ == "__main__":
    unittest.main()
