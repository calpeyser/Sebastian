from music21.stream import Score

class Chorale():

    @staticmethod
    def fromScore(score):
        return Chorale(score)

    def __init__(self, score):
        self.score = score

    def getScore(self):
        return self.score

