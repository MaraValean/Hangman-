# Hangman-
The classical hangman game implemented in python

The computer will select a Sentence that the user can attempt to guess, letter by letter. Each time the user guesses a correct letter, the computer will fill it in the sentence at the correct positions. In case the letter does not appear, the computer will fill in a new letter in the word "hangman", starting from the empty string. The game ends when the user has guessed the sentence (user wins) or when the computer fills in the "hangman" word (user loses).
Program functionality is broken down as follows:

1. Add a sentence. While not in a game, the user can add a sentence 1p]. Each sentence must consist of at least 1 word. Every word in the sentence must have at least 3 letters. There can be no duplicate sentences
3. Start the game. When the user starts a game, the computer selects one of the available sentences and displays it on screen, hangman-style. This means that the computer reveals the first and last letter of every word, as well as all the apparitions of these letters within the words. The sentence selection is random.
e.g. for the sentence "anna has apples", the computer reveals "a__a has a____$
3. Play the game. The game consists of several rounds. In each round, the user proposes a letter. If the sentence contains the letter, the computer reveals where these letters appear within the sentence. If the sentence does not contain the letter, or the user previously proposed the letter the computer will add a new letter to the word "hangman", which is displayed to the user.
Game over. The game is over when the sentence is correctly filled in (user wins), or when the computer fills in the word "hangman" (user loses).

Sentences are loaded from/saved to a text-file that must initially hold at least 5 entries.
