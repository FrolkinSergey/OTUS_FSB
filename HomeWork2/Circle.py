from abc import ABC
from HomeWork2.Figure import Figure
from math import pi


class Circle(Figure, ABC):

    def __init__(self, side_r: int):
        super().__init__(name="Circle")
        if side_r <= 0:
            raise ValueError("Requires value greater than 0")
        self.side_r = side_r

    def get_area(self):
        return round(self.side_r * self.side_r * pi, 3)

    def get_perimetr(self):
        return round(2 * self.side_r * pi, 3)

c = Circle(6)
print(c.get_area())
print(c.get_perimetr())