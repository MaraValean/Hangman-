import unittest

from src.repository.repository import Repository
from src.service.service import Service
from src.service.service_exceptions import ServiceException


class ServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__serv = Service(Repository("tests.txt"))

    def test_add__valid__added(self):
        open("tests.txt", "wt").close()
        self.__serv.add("Good sentence")
        # self.__repo.read_all_from_file()
        self.assertEqual(len(self.__serv.get_sentences()), 1)

    def test_add__invalid__exception(self):
        open("tests.txt", "wt").close()
        # self.__repo.read_all_from_file()
        with self.assertRaises(ServiceException):
            self.__serv.add("Go")

    def tearDown(self) -> None:
        pass
