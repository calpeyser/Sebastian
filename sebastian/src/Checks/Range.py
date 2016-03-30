import music21.note as note

class Range():
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def get_min(self):
        return self.min

    def get_max(self):
        return self.max


