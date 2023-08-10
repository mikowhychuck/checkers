from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, color):
        self.set_color(color)

    def set_color(self, color):
        if color == 'W' or color == 'B':
            self.color = color
            return 0
        else:
            return 1

    def get_color(self):
        return self.color

    @abstractmethod
    def get_symbol(self):
        pass

    @abstractmethod
    def is_move_valid(self):
        pass

    # @abstractmethod
    # def move(self):
    #     pass