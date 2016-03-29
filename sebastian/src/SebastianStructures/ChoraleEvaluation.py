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

    def get_error_list_all(self):
        return self.chorale_error_list

    def get_error_list(self, error_name):
        return [error for error in self.chorale_error_list if error.get_error_name() == error_name]

class ChoraleError(object):
    """
    An error in the chorale.
    """

    def __init__(self, message, notes):
        self.message = message
        self.notes = notes

    def get_message(self):
        return self.message

    def get_error_name(self):
        return "ChoraleError"

    def get_notes(self):
        """
        :return: A list of notes that are "incorrect" subject to this error
        """
        return self.notes