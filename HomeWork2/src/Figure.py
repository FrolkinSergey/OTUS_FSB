from abc import ABC, abstractmethod


class Figure(ABC):
    """Appropriation name"""
    def __init__(self, name):
        self.name = name

    """Area calculation"""
    @abstractmethod
    def get_area(self):
        pass

    """Perimetr calculation"""
    @abstractmethod
    def get_perimetr(self):
        pass

    """Sum areas of several figures """
    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Need class <Figure>")
        return self.get_area() + other_figure.get_area()
