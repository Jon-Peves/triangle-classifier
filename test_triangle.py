import math
from triangle import is_valid_triangle, classify_triangle


def test_is_valid_triangle():
    assert is_valid_triangle(3, 4, 5) == True
    assert is_valid_triangle(1, 1, 2) == False
    assert is_valid_triangle(0, 1, 1) == False
    assert is_valid_triangle(-1, 1, 1) == False


def test_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"


def test_isosceles():
    assert classify_triangle(3, 3, 4) == "Isosceles"
    assert classify_triangle(4, 3, 3) == "Isosceles"
    assert classify_triangle(3, 4, 3) == "Isosceles"


def test_scalene():
    assert classify_triangle(3, 5, 6) == "Scalene"
    assert classify_triangle(4, 5, 6) == "Scalene"
    assert classify_triangle(2, 3, 4) == "Scalene"


def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 12, 13) == "Right Scalene"
    assert classify_triangle(8, 15, 17) == "Right Scalene"
    assert classify_triangle(7, 24, 25) == "Right Scalene"


def test_invalid_zero_or_negative_side():
    assert classify_triangle(0, 3, 4) == "Invalid"
    assert classify_triangle(-1, 3, 4) == "Invalid"
    assert classify_triangle(3, -1, 4) == "Invalid"
    assert classify_triangle(3, 4, -1) == "Invalid"


def test_invalid_inequality_fails():
    assert classify_triangle(1, 2, 8) == "Invalid"
    assert classify_triangle(5, 3, 1) == "Invalid"
    assert classify_triangle(12, 13, 26) == "Invalid"


def test_degenerate_is_invalid():
    assert classify_triangle(1, 1, 2) == "Invalid"
    assert classify_triangle(2, 1, 1) == "Invalid"
    assert classify_triangle(1, 2, 1) == "Invalid"


def test_right_isosceles_non_integer():
    assert classify_triangle(1, 1, math.sqrt(2)) == "Right Isosceles"
    assert classify_triangle(math.sqrt(2), 1, 1) == "Right Isosceles"
    assert classify_triangle(1, math.sqrt(2), 1) == "Right Isosceles"
