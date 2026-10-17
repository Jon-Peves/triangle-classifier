import math


def is_valid_triangle(a, b, c) -> bool:
    if (a <= 0 or b <= 0 or c <= 0):
        return False
    a, b, c = sorted([a, b, c])
    return a+b > c


def classify_triangle(a, b, c) -> str:
    triangle = ""
    if not (is_valid_triangle(a, b, c)):
        return "Invalid"
    if math.isclose(c, a) and math.isclose(c, b):
        return "Equilateral"
    elif math.isclose(a, b) or math.isclose(b, c) or math.isclose(c, a):
        triangle = "Isosceles"
    else:
        triangle = "Scalene"

    a, b, c = sorted([a, b, c])

    if math.isclose(a*a + b*b, c*c):
        triangle = "Right " + triangle

    return triangle
