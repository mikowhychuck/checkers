from cell import Cell
from man import Man
from king import King
from figure import Figure

class Board:
    def __init__(self, color):
        self.cells = None
        self.set_myColor(color)
        self.initialize_cells()

    def set_myColor(self, color):
        if color == 'W' or color == 'B':
            self.myColor = color
            return 0
        else:
            return 1

    def get_my_color(self):
        return self.myColor

    def get_opp_color(self):
        if self.myColor == 'W':
            return 'B'
        elif self.myColor == 'B':
            return 'W'
        else:
            return 1

    def initialize_cells(self):
        self.cells = [Cell(None) for i in range(64)]

        for i in range(0, 7, 2):
            self.cells[i] = Cell(Man('W'))
        for i in range(9, 16, 2):
            self.cells[i] = Cell(Man('W'))
        for i in range(16, 23, 2):
            self.cells[i] = Cell(Man('W'))

        for i in range(41, 47, 2):
            self.cells[i] = Cell(Man('B'))
        for i in range(48, 55, 2):
            self.cells[i] = Cell(Man('B'))
        for i in range(57, 64, 2):
            self.cells[i] = Cell(Man('B'))

    def print_board(self):
        for row in range(7, -1, -1):
            for col in range(8):
                id = row * 8 + col
                if id>9:
                    print(id, end='')
                elif id<=9:
                    print(f" {id}", end='')
                print(self.cells[id], end='')
            print()

    def get_cells(self):
        return self.cells

    def get_cell(self, id):
        return self.cells[id]