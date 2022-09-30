import random

class Puzzle:

    def __init__(self):
        
        self._word_list = open('jumper/game/wordlist.txt').read().splitlines()
        self._word_selected = "hello"
        self._guess_letter = ""
        #while (len(self._word_selected) < 3 or len(self._word_selected) > 8): 
            #self._word_selected = random.choice(self._word_list)

        self._word_guessed = "_" * len(self._word_selected)

    def draw_word_guessed(self):
        print(self._word_guessed)

    def set_guess(self, guess_letter):
        self._guess_letter = guess_letter.lower()

    def process_guess(self):
        _guess_correct = False
        self._word_guessed.strip()

        for i in range(0, len(self._word_selected)):
            if self._guess_letter == self._word_selected[i]:
                _temp_list = list(self._word_guessed)
                _temp_list[i] = self._guess_letter
                self._word_guessed = ''.join(_temp_list)
                _guess_correct = True

        return _guess_correct

    def is_solved(self):
        _solved = False
        if self._word_guessed == self._word_selected:
            _solved = True

        return _solved