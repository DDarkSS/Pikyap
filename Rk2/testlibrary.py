import unittest
from cd import CD
from library import Library

class TestCDLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library(library_id=1, name="Central Library")
        self.cd1 = CD(cd_id=1, title="Abbey Road", artist="The Beatles", genre="Rock")
        self.cd2 = CD(cd_id=2, title="Back in Black", artist="AC/DC", genre="Rock")

    def test_add_cd_to_library(self):
        """Проверка добавления CD в библиотеку."""
        self.library.add_cd(self.cd1)
        self.assertIn(self.cd1, self.library.cds)
        self.assertIn(self.library, self.cd1.libraries)

    def test_add_duplicate_cd_to_library(self):
        """Проверка, что дубликаты CD не добавляются в библиотеку."""
        self.library.add_cd(self.cd1)
        self.library.add_cd(self.cd1)
        self.assertEqual(len(self.library.cds), 1)  # Должен быть только один диск

    def test_multiple_libraries_for_cd(self):
        """Проверка, что один и тот же CD может находиться в разных библиотеках."""
        library2 = Library(library_id=2, name="Community Library")
        self.library.add_cd(self.cd1)
        library2.add_cd(self.cd1)

        self.assertIn(self.cd1, self.library.cds)
        self.assertIn(self.cd1, library2.cds)
        self.assertEqual(len(self.cd1.libraries), 2)  # Должен быть в двух библиотеках

if __name__ == '__main__':
    unittest.main()