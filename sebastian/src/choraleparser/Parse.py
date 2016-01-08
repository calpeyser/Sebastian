from music21 import converter

def parse_from_file(path):
    """
    Parses a chorale from a file, validating that it is in correct form.

    :param path: Absolute path to the musicXML file.
    :return: An instance of Chorale
    """