from re import A


class Jumper:
    """The guy whose parachute is being cut
    
    The responsibility of a Jumper is to provide information related to itself for output and game state conditions

    Attributes:
        _lives_remaining (int): The number of incorrect guesses that can be made
        _draw_list (List): Contains Strings for display throughout gameplay
    """

    def __init__(self):
        """Constructs a new Jumper
        
        Args:
            self (Jumper): an instance of Jumper.
        """

        self._lives_remaining = 4
        self._draw_list = [None] * 5

        self._draw_list[4] = "  ___"
        self._draw_list[3] = " /___\ "
        self._draw_list[2] = " \   /"
        self._draw_list[1] = "  \ / "
        self._draw_list[0] = "   O\n  /|\ \n  / \ "

    def reduce_remaining_lives(self):
        """Decrement lives_remaining
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        self._lives_remaining -= 1

    def draw_jumper(self):
        """Prints the contents of draw_list with respect to the number of lives remaining
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        print("\n")
        for i in range (self._lives_remaining, -1, -1):
            print(self._draw_list[i])

    def is_alive(self):
        """Checks to see if Jumper is out of lives. If so, his head becomes an X
        
        Args:
            self (Jumper): an instance of Jumper.
        """
        if self._lives_remaining == 0:
            self._draw_list[0] = "   X\n  /|\ \n  / \ "
            return False
        else:
            return True