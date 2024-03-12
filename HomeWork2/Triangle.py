from abc import ABC
from HomeWork2.Figure import Figure
from math import sqrt


class Triangle(Figure, ABC):

    def __init__(self, side_a: int, side_b: int, side_c: int):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Requires value greater than 0")
        if (side_a + side_b) <= side_c or (side_a + side_c) <= side_b or (side_b + side_c) <= side_a:
            raise ValueError("Create a triangle is impossible")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.p = self.get_perimetr() / 2

    def get_area(self):
        return round(sqrt(self.p * (self.p - self.side_a) * (self.p - self.side_b) * (self.p - self.side_c)), 2)

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c

c = Triangle(6, 6, 6)
print(c.get_area())
print(c.get_perimetr())
print