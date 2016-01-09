class ChoraleEvaluation():

    def __init__(self, chorale):
        self.chorale = chorale
        self.chorale_error_list = ChoraleErrorList()


class ChoraleErrorList():

    def __init__(self):
        self.error_list = []

    def add_error(self, error):
        self.error_list.append(error)


class ChoraleError():

    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message