from figure import Figure
from movement import Movement


class Man(Figure):
    def __init__(self, color):
        super().__init__(color)

    def get_symbol(self):
        if super().get_color() == 'W':
            return '\u26C0'
        elif super().get_color() == 'B':
            return '\u26C2'
        else:
            return 1

    def is_move_valid(self, movement, board):
        if super().get_color() == 'W':
            self.dir = 1
        elif super().get_color() == 'B':
            self.dir = -1
        else:
            self.dir = 0
        self.id_from = movement.get_id_from()
        self.id_to = movement.get_id_to()
        if self.id_to == self.id_from + (7 * self.dir) or self.id_to == self.id_from + (9 * dir):
            if board.get_cell(self.id_to).get_figure is None:
                return True
        else:
            return False
