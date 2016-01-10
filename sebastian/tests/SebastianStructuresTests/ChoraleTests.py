from sebastian.src.SebastianParser import SebastianParser
import sebastian.tests.testfiles.TestFilePaths as TestFilePaths
from sebastian.src.SebastianStructures import Constants
from music21.pitch import Pitch

import unittest

class ChoraleTests(unittest.TestCase):

    def setUp(self):
        parser = SebastianParser(TestFilePaths.basic_chorale)
        self.chorale = parser.parse_as_chorale()

    def test_NoteMaps(self):
        soprano_note_map =  self.chorale.get_note_map(Constants.SOPRANO_PART_NUMBER)
        soprano_note_list = self.chorale.get_note_list(Constants.SOPRANO_PART_NUMBER)

        self.assertEqual(0.0, soprano_note_map[soprano_note_list[0]])
        self.assertEqual(1.0, soprano_note_map[soprano_note_list[1]])
        self.assertEqual(3.0, soprano_note_map[soprano_note_list[2]])
        self.assertEqual(4.0, soprano_note_map[soprano_note_list[3]])
        self.assertEqual(5.5, soprano_note_map[soprano_note_list[4]])
        self.assertEqual(6.0, soprano_note_map[soprano_note_list[5]])

    def test_NoteListsContainAllNotes(self):
        soprano_note_list = self.chorale.get_note_list(Constants.SOPRANO_PART_NUMBER)
        alto_note_list = self.chorale.get_note_list(Constants.ALTO_PART_NUMBER)
        tenor_note_list = self.chorale.get_note_list(Constants.TENOR_PART_NUMBER)
        bass_note_list = self.chorale.get_note_list(Constants.BASS_PART_NUMBER)

        self.assertEqual(46, len(soprano_note_list))
        self.assertEqual(58, len(alto_note_list))
        self.assertEqual(59, len(tenor_note_list))
        self.assertEqual(60, len(bass_note_list))

    def test_NoteMapsContainAllNotes(self):
        soprano_note_map = self.chorale.get_note_map(Constants.SOPRANO_PART_NUMBER)
        alto_note_map = self.chorale.get_note_map(Constants.ALTO_PART_NUMBER)
        tenor_note_map = self.chorale.get_note_map(Constants.TENOR_PART_NUMBER)
        bass_note_map = self.chorale.get_note_map(Constants.BASS_PART_NUMBER)

        self.assertEqual(46, len(soprano_note_map))
        self.assertEqual(58, len(alto_note_map))
        self.assertEqual(59, len(tenor_note_map))
        self.assertEqual(60, len(bass_note_map))

    def test_GetNoteAtOffset(self):
        self.assertEqual(Pitch("G4"), self.chorale.get_note_at_offset(Constants.SOPRANO_PART_NUMBER, 0.0).pitch)
        self.assertEqual(Pitch("G4"), self.chorale.get_note_at_offset(Constants.SOPRANO_PART_NUMBER, 1.5).pitch)


if __name__ == "__main__":
    unittest.main()