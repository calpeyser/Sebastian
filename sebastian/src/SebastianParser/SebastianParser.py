from .. import SebastianStructures
from SebastianParsingException import SebastianParsingException

from music21 import converter
from music21 import stream

class SebastianParser():

    def __init__(self, path):
        self.path = path
        self.validators = [
            self.validate_is_score,
            self.validate_has_four_parts
        ]

    def parse_as_chorale(self):
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