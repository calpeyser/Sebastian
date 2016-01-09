from .. import SebastianStructures
from music21 import converter

class SebastianParser():

    def __init__(self, path):
        self.path = path

    def parse_as_chorale(self):
        self.parsed_input = converter.parse(path)
        self.validate(self.parsed_input)
        return self.parsed_input

    def validate(self):
        pass
