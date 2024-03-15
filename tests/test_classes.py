from math import sqrt, pi
import pytest
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


@pytest.mark.rectangle
@pytest.mark.positive
@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [
                             (1, 1, 1),
                             (4, 4, 16),
                             (6.3, 6.6, 41.58),
                         ],
                         ids=["integer", "integer", "float"])
def test_area_rectangle_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area, f"Area should be {side_a * side_b}"


@pytest.mark.rectangle
@pytest.mark.positive
@pytest.mark.parametrize(("side_a", "side_b", "perimetr"),
                         [
                             (1, 1, 4),
                             (3, 4, 14),
                             (6, 6.6, 25.2),
                         ],
                         ids=["integer", "integer", "float"])
def test_perimetr_rectangle_positive(side_a, side_b, perimetr):
    r = Rectangle(side_a, side_b)
    assert r.get_perimetr() == perimetr, f"Perimetr should be {side_a * side_b}"


@pytest.mark.rectangle
@pytest.mark.negative
@pytest.mark.parametrize(("side_a", "side_b"),
                         [
                             (0, 1),
                             (4, 0),
                             (-1, 2),
                             (3, -2)
                         ],
                         ids=["a = 0", "b = 0", "a < 0", "b < 0"])
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.square
@pytest.mark.positive
@pytest.mark.parametrize(("side_a", "area"),
                         [
                             (1, 1),
                             (3, 9),
                             (4.5, 20.25),
                         ],
                         ids=["integer", "integer", "float"])
def test_area_square_positive(side_a, area):
    s = Square(side_a)
    assert s.get_area() == area, f"Area should be {side_a * side_a}"


@pytest.mark.square
@pytest.mark.positive
@pytest.mark.parametrize(("side_a", "perimetr"),
                         [
                             (1, 4),
                             (3.7, 14.8),
                         ],
                         ids=["integer", "float"])
def test_perimetr_square_positive(side_a, perimetr):
    s = Square(side_a)
    assert s.get_perimetr() == perimetr, f"Perimetr should be {side_a * side_a}"


@pytest.mark.square
@pytest.mark.negative
@pytest.mark.parametrize("side_a",
                         [
                             (0), (-1),
                         ],
                         ids=["a = 0", "a < 0"])
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.triangle
@pytest.mark.positive
@pytest.mark.parametrize("triangle_data", ["integer", "float"])
def test_area_triangle_positive_int(triangle_area_data, triangle_data):
    side_a, side_b, side_c, area = triangle_area_data(data=triangle_data)
    t = Triangle(side_a, side_b, side_c)
    p = t.get_perimetr() / 2
    assert t.get_area() == area, f"Area should be {round(sqrt(p * (p - side_a) * (p - side_b)* (p - side_c)), 2)}"


@pytest.mark.triangle
@pytest.mark.positive
def test_perimetr_triangle_positive_int(triangle_perimetr_data_int):
    side_a, side_b, side_c, perimetr = triangle_perimetr_data_int
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimetr() == perimetr, f"Perimetr should be {side_a + side_b + side_c}"


@pytest.mark.triangle
@pytest.mark.positive
def test_perimetr_triangle_positive_flot(triangle_perimetr_data_flot):
    side_a, side_b, side_c, perimetr = triangle_perimetr_data_flot
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimetr() == perimetr, f"Perimetr should be {side_a + side_b + side_c}"


@pytest.mark.triangle
@pytest.mark.negative
@pytest.mark.parametrize(("side_a", "side_b", "side_c"),
                         [
                             (0, 1, 2), (2, 0, 3), (3, 4, 0),
                             (-1, 2, 3), (3, -2, 4), (1, 3, -4)
                         ],
                         ids=["a = 0|b,c > 0", "b = 0|a,c > 0", "c = 0|a,b > 0",
                              "a < 0|b,c > 0", "b < 0|a,c > 0", "c < 0|a,b > 0"])
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.circle
@pytest.mark.positive
@pytest.mark.parametrize("circle_data", ["integer", "float"])
def test_area_circle_positive_int(circle_area_data, circle_data):
    side_r, area = circle_area_data(data=circle_data)
    c = Circle(side_r)
    assert c.get_area() == area, f"Area should be {round(side_r * side_r * pi, 3)}"


@pytest.mark.circle
@pytest.mark.positive
@pytest.mark.parametrize("circle_data", ["integer", "float"])
def test_perimetr_circle_positive_int(circle_perimetr_data, circle_data):
    side_r, perimetr = circle_perimetr_data(data=circle_data)
    c = Circle(side_r)
    assert c.get_perimetr() == perimetr, f"Area should be {round(2 * side_r * pi, 3)}"


@pytest.mark.circle
@pytest.mark.negative
@pytest.mark.parametrize("circle_data", ["zero", "below_zero"])
def test_circle_negative(circle_negative_data, circle_data):
    side_r = circle_negative_data(data=circle_data)
    with pytest.raises(ValueError):
        Circle(side_r)
