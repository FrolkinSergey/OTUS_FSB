from abc import ABC, abstractmethod


class Figure(ABC):
    """Appropriation name"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_area(self):
        """Area calculation"""
        pass

    @abstractmethod
    def get_perimetr(self):
        """Perimetr calculation"""
        pass

    def add_area(self, other_figure):
        """Sum areas of several figures """
        if not isinstance(other_figure, Figure):
            raise ValueError("Need class <Figure>")
        return self.get_area() + other_figure.get_area()
