from sebastian.src.SebastianParser import SebastianParser
import unittest

class BasicParsingTests(unittest.TestCase):

    def test_CanConstruct(self):
        try:
            parser = SebastianParser("../testfiles/basic_chorale.xml")
        except Exception:
            self.fail("SebastianParser threw exception on construction")

    def test_CanParse(self):
        try:
            parser = SebastianParser("../testfiles/basic_chorale.xml")
            parser.parse_as_chorale()
        except Exception as e:
            self.fail("SebastianParser threw exception on parsing: " + e.message)


if __name__ == "__main__":
    unittest.main()