class ChoraleEvaluation():
    """
    A mutable data structure giving the state of the chorale analysis.
    """

    def __init__(self, chorale, check_list):
        self.chorale = chorale
        self.chorale_error_list = []
        self.check_list = check_list

    def evaluate(self):
        for check in self.check_list:
            errors_from_check = check.run_check(self.chorale)
            self.chorale_error_list.extend(errors_from_check)

    def get_error_list(self):
        return self.chorale_error_list

class ChoraleError():
    """
    An error in the chorale.
    """

    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message