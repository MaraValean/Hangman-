import random

from src.service.service_exceptions import ServiceException
from src.service.validators import Validator


class Service:
    def __init__(self,repo):
        self.__repository = repo
        self.__validator = Validator()

    def add(self,sentence):
        if not self.__validator.validate_sentence(sentence):
            raise ServiceException("The sentence cannot be added because it doesn't respect the format (at least one word, each word having at least 3 letters)")
        else:
            self.__repository.add(sentence)

    def get_sentences(self):
        sentences = self.__repository.get_sentences()
        return sentences

    def select_sentence(self):
        sentences = self.get_sentences()
        index = random.randint(0,len(sentences)-1)
        sentence = sentences[index]
        return sentence

    @staticmethod
    def format_sentence(sentence):
        final_sentence = ""
        words = sentence.split()
        for word in words:
            first = word[0]
            last = word[-1]
            for letter in word:
                if letter == first or letter == last :
                    final_sentence += letter
                else:
                    final_sentence += "_"
            final_sentence += " "
        return final_sentence

    @staticmethod
    def write_guess(guess,sentence,game_sentence):
        final_sentence =""
        for letter in sentence:
            if letter == guess or letter in game_sentence:
                final_sentence += letter
            else:
                final_sentence += "_"
        return final_sentence

    @staticmethod
    def display_hangman( hangman_index):
        hangman = "hangman"
        display_hangman = ""
        for i in range(hangman_index):
            display_hangman += hangman[i]
        return display_hangman
