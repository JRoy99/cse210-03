class Jumper:

    def __init__(self):

        self._lives_remaining = 5
        self._draw_list = [None] * 5

        self._draw_list[4] = " ___"
        self._draw_list[3] = "/___\ "
        self._draw_list[2] = "\   /"
        self._draw_list[1] = " \ / "
        self._draw_list[0] = "  O\n  /|\ \n  / \ "

    def reduce_remaining_lives(self):
        self._lives_remaining -= 1

    def draw_jumper(self):
        for i in range (self._lives_remaining, 0, -1):
            print(self._draw_list[1])

    def is_alive(self):
        if self._lives_remaining == 0:
            self._draw_list[0] = "  X\n  /|\ \n  / \ "
            return False
        else:
            return True