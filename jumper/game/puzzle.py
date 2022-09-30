import random

class Puzzle:

    def __init__(self):
        
        self._word_list = open('wordlist.txt').read().splitlines()
        self._word_selected = ""
        self._guess_letter = ""
        while len(self._word_selected) < 3: 
            self._word_selected = random.choice(self._word_list)

        self._word_guessed = "_ " * len(self._word_selected)

    def draw_word_guessed(self):
        print(self._word_guessed)

    def set_guess(self, guess_letter):
        self._guess_letter = guess_letter

    def process_guess(self):
        _guess_correct = True
        if self._guess_letter not in self._word_selected:
            _guess_correct = False

        return _guess_correct

    def is_solved(self):
        _solved = True

        for i in self._word_guessed:
            if i not in self._word_selected:
                _solved = False

        return _solved