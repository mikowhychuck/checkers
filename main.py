from board import Board
from movement import Movement
b = Board('W')
b.print_board()
m = Movement(22, 29)
b.get_cell(22).get_figure.is_move_valid(m)