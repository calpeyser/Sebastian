from sebastian.src.SebastianParser.SebastianParser import SebastianParser
from sebastian.src.SebastianStructures.ChoraleEvaluation import ChoraleEvaluation
from sebastian.src.Checks.ParallelUnisonCheck import ParallelUnisonCheck
from sebastian.src.Checks.ParallelFifthCheck import ParallelFifthCheck
from sebastian.src.Checks.ParallelOctaveCheck import ParallelOctaveCheck
from sebastian.src.Checks.RepBassCheck import RepBassCheck
from sebastian.src.Checks.RangeCheck import RangeCheck
from sebastian.src.Checks.TritoneJumpCheck import TritoneJumpCheck
from sebastian.src.Checks.VoiceCrossingCheck import VoiceCrossingCheck
from sebastian.src.Checks.DistanceBetweenVoicesCheck import DistanceBetweenVoicesCheck

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
        Populates this chorale's evaluation with a list of errors.
        """
        self.evaluation.evaluate()

    def get_error_list_all(self):
        """
        :return: Errors from this analysis
        """
        return self.evaluation.get_error_list_all()

    def get_error_list(self, error_name):
        """
        :param error_name: Error type
        :return: A list of errors from this analysis of this type.
        """
        return self.evaluation.get_error_list(error_name)

    def check_list(self):
        """
        :return: A list of checks to be implemented in this analysis.  Should be overridden by
        implementation.
        """
        pass

    def get_annotated_chorale(self):
        """
        :return: A string giving musicXML for this chorale, with colors applied for mistakes.
        """
        self.chorale.annotate_chorale(self.get_error_list_all())
        return self.chorale

class MockChoraleAnalysis(ChoraleAnalysis):
    """
    An implementation of ChoraleAnalysis with no checks.
    """

    def check_list(self):
        return []

class XMLChoraleAnalysis(ChoraleAnalysis):
    """
    An implmenation of ChoraleAnalysis that performs all checks available with only a MusicXML file.
    """

    def check_list(self):
        return [
            #ParallelUnisonCheck(),
            #ParallelFifthCheck(),
            #ParallelOctaveCheck(),
            RangeCheck(),
            RepBassCheck(),
            TritoneJumpCheck(),
            #VoiceCrossingCheck(),
            DistanceBetweenVoicesCheck()
        ]