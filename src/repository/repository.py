from src.repository.repository_exceptions import RepoException


class Repository:
    def __init__(self,file_path):
        self.__sentences = []
        self.__file_path = file_path

    def write_all_to_file(self):
        file = open(self.__file_path, 'wt')
        for entity in self.__sentences:
            file.write(entity.strip() + '\n')
        file.close()

    def read_all_from_file(self):
        file = open(self.__file_path, 'rt')  # with open(self.__file_path, 'r') as file:
        self.__sentences.clear()
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if len(line):  # to avoid reading the last empty line
                self.__sentences.append(line)
        file.close()

    def search(self,sentence):
        self.read_all_from_file()
        for entity in self.__sentences:
            if entity == sentence:
                return True
        return False

    def get_sentences(self):
        self.read_all_from_file()
        return self.__sentences

    def add(self,sentence):
        if self.search(sentence):
            raise RepoException("This sentence cannot be added because it already exits!")
        else:
            self.__sentences.append(sentence)
            self.write_all_to_file()
