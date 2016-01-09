from sebastian.src.ChoraleAnalysis.ChoraleAnalysis import MockChoraleAnalysis
import sebastian.tests.testfiles.TestFilePaths as TestFilePaths

import unittest

class BasicIntegrationTests(unittest.TestCase):

    def test_CanConstructBasicAnalysis(self):
        try:
            analysis = MockChoraleAnalysis(TestFilePaths.basic_chorale)
        except Exception:
            self.fail("Cannot construct MockChoraleAnalysis")

    def test_CanRunBasicAnalysis(self):
        analysis = MockChoraleAnalysis(TestFilePaths.basic_chorale)

        try:
            analysis.analyze()
        except Exception:
            self.fail("Cannot run MockChoraleAnalysis")

    def test_MockAnalysisReturnsNoErrors(self):
        analysis = MockChoraleAnalysis(TestFilePaths.basic_chorale)
        analysis.analyze()
        error_list = analysis.get_error_list()

        self.assertEqual([], error_list)

if __name__ == "__main__":
    unittest.main()