from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle
import string


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        jumper (Jumper): The game's jumper.
        is_playing (boolean): Whether or not to keep playing.
        seeker (puzzle): The game's Puzzle.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._jumper = Jumper()
        self._is_playing = True
        self._puzzle = Puzzle()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._do_outputs()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Gets and validates user input, storing in puzzle

        Args:
            self (Director): An instance of Director.
        """
        _invalid_guess = True
        while _invalid_guess:
            _guess_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
            self._puzzle.set_guess(_guess_letter)

            if (_guess_letter in string.ascii_letters and 
            _guess_letter not in self._puzzle.get_guess_list() and
            len(_guess_letter) <= 1):
                _invalid_guess = False
            else:
                self._terminal_service.write_text("Invalid Input. Please select an unused letter.")
        
        
    def _do_updates(self):
        """Checks if guess was correct. If not, reduces jumper lives. Checks multiple end-state conditions

        Args:
            self (Director): An instance of Director.
        """
        if not self._puzzle.process_guess():
            self._jumper.reduce_remaining_lives()
            self._is_playing = self._jumper.is_alive()
        else:
            if self._puzzle.is_solved():
                self._is_playing = False
                
        
    def _do_outputs(self):
        """Displays current guessed word, the jumper, and all guessed letters to user.
           Also displays end game messages

        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.draw_word_guessed()
        self._jumper.draw_jumper()
        self._terminal_service.write_text("\n^^^^^^^")
        print(''.join(self._puzzle.get_guess_list()))

        if self._is_playing == False:
            if self._jumper.is_alive() == False:
                self._terminal_service.write_text("Game Over. The word was " + 
                self._puzzle._word_selected + ".")
            else:
                self._terminal_service.write_text("You Win!")