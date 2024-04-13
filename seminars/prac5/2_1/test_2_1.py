import pytest
from testing_code import triangle_type, triangle_type_correct

print("\033[42mВаша функция:\033[0m")


def test_equilateral_triangle():
    assert triangle_type(0, 0, 4, 0, 2, 2 * (3 ** 0.5)) == "равносторонний"


def test_isosceles_triangle():
    assert triangle_type(0, 0, 2, 0, 1, 2) == "равнобедренный"


def test_scalene_triangle():
    assert triangle_type(0, 0, 2, 0, 2, 2) == "разносторонний"


def test_identical_points():
    assert triangle_type(0, 0, 0, 0, 0, 0) == "не существует"


print("\033[42mМоя функция:\033[0m")


def test_equilateral_triangle_correct():
    assert triangle_type_correct(0, 0, 4, 0, 2, 2 * (3 ** 0.5)) == "равносторонний"


def test_isosceles_triangle_correct():
    assert triangle_type_correct(0, 0, 2, 0, 1, 2) == "равнобедренный"


def test_scalene_triangle_correct():
    assert triangle_type_correct(0, 0, 2, 0, 2, 2) == "разносторонний"


def test_identical_points_correct():
    assert triangle_type_correct(0, 0, 0, 0, 0, 0) == "не существует"
