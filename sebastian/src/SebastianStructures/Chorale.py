from music21.stream import Score


class Chorale():
    """
    A wrapper over a music21.stream.Score instance that represents the chorale under evaluation.
    """

    @staticmethod
    def fromScore(score):
        """
        Static constructor.

        :param score: A score, likely the result of a parsing.
        :return: A Chorale instance wrapping the score.
        """
        return Chorale(score)

    def __init__(self, score):
        self.score = score

    def getScore(self):
        """
        :return: The score wrapped by this Chorale instance.
        """
        return self.score

