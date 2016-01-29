class SebastianParsingException(Exception):
    """
    Indicates that a MusicXML file could not be parsed into a chorale.
    """

    def __init__(self, message):
        super(SebastianParsingException, self).__init__(message)