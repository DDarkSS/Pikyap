import unittest
from Rk1 import CD, Library

class TestCDLibrary(unittest.TestCase):

    def test_cd_creation(self):
        cd = CD(1, "Thriller", "Michael Jackson", "Pop", 1)
        self.assertEqual(cd.cd_id, 1)
        self.assertEqual(cd.title, "Thriller")
        self.assertEqual(cd.artist, "Michael Jackson")
        self.assertEqual(cd.genre, "Pop")
        self.assertEqual(cd.library_id, 1)

    def test_library_creation(self):
        library = Library(1, "Central Library")
        self.assertEqual(library.library_id, 1)
        self.assertEqual(library.name, "Central Library")
        self.assertEqual(len(library.cds), 0)

    def test_adding_cd_to_library(self):
        library = Library(1, "Central Library")
        cd = CD(1, "Thriller", "Michael Jackson", "Pop", 1)
        library.add_cd(cd)
        self.assertEqual(len(library.cds), 1)
        self.assertEqual(library.cds[0].title, "Thriller")

if __name__ == "__main__":
    unittest.main()