import math
from triangle import classify_triangle, is_valid_triangle


def test_classify_triangle():
    # Non right triangles return a shape
    assert classify_triangle(5, 5, 5) == "Equilateral"
    assert classify_triangle(2, 2, 3) == "Isosceles"
    assert classify_triangle(3, 4, 6) == "Scalene"

    # Not valid Triangle returns Invalid instead of an error
    assert classify_triangle(0, 1, 1) == "Invalid"
    assert classify_triangle(-1, 1, 1) == "Invalid"
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(1, 1, 3) == "Invalid"

    # Right triangles return a shape
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(1, 1, math.sqrt(2)) == "Right Isosceles"
