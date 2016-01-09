from Sebastian.src.SebastianParser import SebastianParser
from ChoraleEvaluation import ChoraleEvaluation

class ChoraleAnalysis():
    """
    Provides access to the Sebastian library.  Can be serialized for use in creating an
    API to Sebastian.
    """

    def __init__(self, XML_path, RNA_path = None):
        """
        :param XML_path: Path to MusicXML to analyze.
        :param RNA_path: Optional path to RNA
        """
        self.XML_path = XML_path
        self.RNA_path = RNA_path
        self.chorale = SebastianParser(XML_path).parse_as_chorale()
        self.evaluation = ChoraleEvaluation(self.chorale)

    def analyze(self):
        """
        :return: A list of errors
        """
        self.evaluation.evaluate()

