from src.Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a: int):
        super().__init__(side_a, side_a)
