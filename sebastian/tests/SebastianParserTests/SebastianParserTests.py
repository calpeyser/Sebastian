from ...src import SebastianParser
import unittest

class BasicParsingTests(unittest.TestCase):

    def test_CanConstruct(self):
        parser = SebastianParser("../testfiles/basic_chorale.xml")

if __name__ == "__main__":
    unittest.main()