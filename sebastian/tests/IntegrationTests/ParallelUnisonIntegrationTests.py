from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import XMLChoraleAnalysis
import sebastian.tests.testfiles.TestFilePaths as TestFilePaths

import unittest

class BasicIntegrationTests(unittest.TestCase):

    def test_ThrowsErrorWithParallelUnisons(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.parallel_unison)
        analysis.analyze()
        self.assertNotEqual([], analysis.get_error_list())

    def test_CorrectPropertiesOnParallelUnisonError(self):
        analysis = XMLChoraleAnalysis(TestFilePaths.parallel_unison)
        analysis.analyze()
        self.assertEqual("Unison", analysis.get_error_list()[0].get_interval_name())

if __name__ == "__main__":
    unittest.main()