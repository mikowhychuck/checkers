from figure import Figure

class King(Figure):
    def __init__(self, color):
        super().__init__(color)

    def get_symbol(self):
        if super().color == 'W':
            return '\u26C1'
        elif super().color == 'B':
            return '\u26C3'
        else:
            return 1