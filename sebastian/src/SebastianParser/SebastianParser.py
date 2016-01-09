from .. import SebastianStructures
from SebastianParsingException import SebastianParsingException

from music21 import converter
from music21 import stream

class SebastianParser():
    """
    Parses a MusicXML file in to a chorale.  Performs validation to ensure that the chorale
    can be analyzed by Sebastian.

    Should be implemented with a group of "validator" functions, which check a condition on the
    chorale.  Each validator is run, with a failed validator throwing a SebastianParsingException.
    """

    def __init__(self, path):
        self.path = path
        self.validators = [
            self.validate_is_score,
            self.validate_has_four_parts
        ]

    def parse_as_chorale(self):
        """
        Throws a SebastianParsingException if the chorale is malformed.

        :return: A chorale instance.
        """
        self.parsed_input = converter.parse(self.path)
        self.validate()
        return SebastianStructures.Chorale(self.parsed_input)

    def validate(self):
        for validator in self.validators:
            if not validator():
                raise SebastianParsingException("Parsing Failure: " + validator.__name__)

    def validate_is_score(self):
        return isinstance(self.parsed_input, stream.Score)

    def validate_has_four_parts(self):
        return len(self.parsed_input.parts) == 4