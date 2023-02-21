import unittest

from src.repository.repository import Repository
from src.repository.repository_exceptions import RepoException


class RepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = Repository("tests.txt")

    def test_add__valid__added(self):
        open("tests.txt", "wt").close()
        self.__repo.add("Good sentence")
        #self.__repo.read_all_from_file()
        self.assertEqual(len(self.__repo.get_sentences()),1)

    def test_add__invalid__exception(self):
        open("tests.txt", "wt").close()
        self.__repo.add("Good sentence")
        #self.__repo.read_all_from_file()
        with self.assertRaises(RepoException):
            self.__repo.add("Good sentence")

    def test_read_all_from_file(self):
        open("tests.txt", "wt").close()
        self.__repo.add("Good sentence")
        self.__repo.read_all_from_file()
        self.assertEqual(len(self.__repo.get_sentences()),1)

    def test_write_all_to_file(self):
        open("tests.txt", "wt").close()
       # self.__repo.get_questions().clear()
        self.__repo.add("Good sentence")
        self.__repo.write_all_to_file()
        self.assertEqual(len(self.__repo.get_sentences()),1)

    def test_search_valid(self):
        open("tests.txt", "wt").close()
        self.__repo.add("Good sentence")
        self.assertEqual( self.__repo.search("Good sentence") , True)

    def test_search_invalid(self):
        open("tests.txt", "wt").close()
        self.__repo.add("Good sentence")
        self.assertEqual(self.__repo.search("Good sentenc"), False)

    def test_get_sentences(self):
        open("tests.txt", "wt").close()
        self.__repo.add("Good sentence")
        self.__repo.add("Another one")
        self.__repo.add("Third")
        sentences = self.__repo.get_sentences()
        self.assertEqual(len(sentences), 3)

    def tearDown(self) -> None:
        pass
