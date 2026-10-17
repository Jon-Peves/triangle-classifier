import math


def is_valid_triangle(a, b, c) -> bool:
    if (a <= 0 or b <= 0 or c <= 0):
        return False
    a, b, c = sorted([a, b, c])
    return a+b > c


def classify_triangle(a, b, c) -> str:

    return "valid"
