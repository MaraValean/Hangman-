from src.repository.repository_exceptions import RepoException
from src.service.service_exceptions import ServiceException


class Ui:
    def __init__(self,serv):
        self.__service = serv

    @staticmethod
    def display_menu():
        print("HANGMAN GAME")
        print("You can add a new sentence, play the game or exit")
        print("1. add a sentence")
        print("2. play game")
        print("0. exit")

    def play_game(self):
        sentence = self.__service.select_sentence()
        hangman_index = 0
        game_sentence = self.__service.format_sentence(sentence)
        print(game_sentence)
        print("Your hangman this far is: " + self.__service.display_hangman(hangman_index))
        while hangman_index<7 and sentence != game_sentence :
            guess = input("Type your guess letter> ").strip()
            if guess in sentence and guess not in game_sentence:
                game_sentence = self.__service.write_guess(guess, sentence,game_sentence)
            else:
                hangman_index += 1
            print(game_sentence)
            print("Your hangman this far is: " + self.__service.display_hangman(hangman_index))
        if hangman_index == 7:
            print("GAME OVER...you lost")
        if sentence == game_sentence:
            print("CONGRATULATIONS...you won")

    def add(self):
        sentence = input("Please type in the sentence you want to add> ")
        sentence = sentence.strip()
        try:
            self.__service.add(sentence)
            print("Sentence added successfully!")
        except RepoException as re:
            print(re)
        except ServiceException as se:
            print(se)

    def choose_option(self):
        option = input("Choose option> ")
        if option == "1":
            self.add()
        elif option == "0":
            exit()
        elif option == "2":
            self.play_game()
        else:
            print("Invalid option!")

    def start(self):
        while True:
            self.display_menu()
            self.choose_option()