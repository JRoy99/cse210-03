import random

class Puzzle:
    """A word to be guessed and related information
    
    The responsibility of a Puzzle is to store and process information related to letter input and the word to guess.

    Attributes:
        _word_list (List): List of words available to choose from
        _word_selected (String): Contains the string selected from the list
        _guess_letter (String): The letter guessed by the player
        _guess_list (List): Contains all previously made guesses
    """

    def __init__(self):
        """Constructs a new Puzzle. Selects a word between length 3 and 8
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        
        self._word_list = open('jumper/game/wordlist.txt').read().splitlines()
        self._word_selected = ""
        self._guess_letter = ""
        self._guess_list = []

        while (len(self._word_selected) < 3 or len(self._word_selected) > 8): 
            self._word_selected = random.choice(self._word_list)

        self._word_guessed = "_ " * len(self._word_selected)

    def draw_word_guessed(self):
        """Displays the current word guess
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        print(self._word_guessed)

    def set_guess(self, guess_letter):
        """Sets the guessed letter to passed input converted to lowercase
        
        Args:
            self (Puzzle): an instance of Puzzle.
            guess_letter (String): Letter inputted in terminal
        """
        self._guess_letter = guess_letter.lower()

    def get_guess_list(self):
        """Retrieves list of guessed letters for input validation and display
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        return self._guess_list

    def process_guess(self):
        """Converts word_guessed to list. Checks each letter in word_selected against the guessed letter.
           If a match is found, change the value in list(word_guessed) to the guessed letter.
           Convert list(word_guessed) back into string with formatting.
           If a match was found, return true. Otherwise, return false
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        _guess_correct = False
        self._guess_list.append(self._guess_letter)

        _temp_list = list(self._word_guessed.replace(" ",""))

        for i in range(0, len(self._word_selected)):
            if self._guess_letter == self._word_selected[i]:
                _temp_list[i] = self._guess_letter + " "
                _guess_correct = True
            else:
                _temp_list[i] += " "
        self._word_guessed = ''.join(_temp_list)
        return _guess_correct

    def is_solved(self):
        """Checks if the puzzle has been solved by comparing word_guessed against word_selected
        
        Args:
            self (Puzzle): an instance of Puzzle.
        """
        _solved = False
        if self._word_guessed.replace(" ","") == self._word_selected:
            _solved = True

        return _solved