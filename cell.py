from figure import Figure

class Cell:
    def __init__(self, figure):
        self.set_figure(figure)

    def set_figure(self, figure):
        if isinstance(figure, Figure) or figure is None:
            self.figure = figure
            return 0
        else:
            return 1;

    def get_figure(self):
        return self.figure

    def __str__(self):
        if self.figure is None:
            return '\u25A1 '
        else:
            return self.get_figure().get_symbol() + ' '

    def get_symbol(self):

        if self.figure is None:
            return '\u25A1'
        else:
            return self.get_figure().get_symbol()