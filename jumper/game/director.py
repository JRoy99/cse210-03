from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
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
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        guess_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._puzzle.set_guess(guess_letter)
        
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

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
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        self._puzzle.draw_word_guessed()
        self._jumper.draw_jumper()
        self._terminal_service.write_text("\n^^^^^^^")

        if self._is_playing == False:
            if self._jumper.is_alive() == False:
                self._terminal_service.write_text("Game Over. The word was " + 
                self._puzzle._word_selected)
            else:
                self._terminal_service.write_text("You Win!")