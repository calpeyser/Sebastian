from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import XMLChoraleAnalysis
import sebastian.tests.testfiles.TestFilePaths as TestFilePaths
from sebastian.src.Utils.Utils import *

import unittest

class BasicIntegrationTests(unittest.TestCase):

    def test_ThrowsErrorWithParallelUnisons(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.parallel_unison)
        analysis.analyze()
        errors = analysis.get_error_list("ParallelUnisonError")
        self.assertEqual(1, len(errors))

    def test_CorrectPropertiesOnParallelUnisonError(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.parallel_unison)
        analysis.analyze()
        error = get_only_element(analysis.get_error_list("ParallelUnisonError"))

        self.assertEqual("Unison", error.get_interval_name())

if __name__ == "__main__":
    unittest.main()