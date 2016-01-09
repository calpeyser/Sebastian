from sebastian.src.SebastianParser.SebastianParser import SebastianParser
from sebastian.src.SebastianStructures.ChoraleEvaluation import ChoraleEvaluation

class ChoraleAnalysis():
    """
    Provides access to the Sebastian library.  Can be serialized for use in creating an
    API to Sebastian.

    This class should not be instantiated.
    """

    def __init__(self, XML_path, RNA_path = None):
        """
        :param XML_path: Path to MusicXML to analyze.
        :param RNA_path: Optional path to RNA
        """
        self.XML_path = XML_path
        self.RNA_path = RNA_path
        self.chorale = SebastianParser(XML_path).parse_as_chorale()
        self.evaluation = ChoraleEvaluation(self.chorale, self.check_list())

    def analyze(self):
        """
        :return: A list of errors
        """
        self.evaluation.evaluate()

    def get_error_list(self):
        return self.evaluation.get_error_list()

    def check_list(self):
        """
        :return: A list of checks to be implemented in this analysis.  Should be overridden by
        implementation.
        """
        pass

class MockChoraleAnalysis(ChoraleAnalysis):
    """
    An implementation of ChoraleAnalysis with no checks.
    """

    def check_list(self):
        return []