import math

import pytest
from lab4_oop.tasks.task1 import Triangle, Equilateral


def test_triangle_creation():
    t = Triangle(3, 4, 5)
    assert t.a == 3
    assert t.b == 4
    assert t.c == 5


def test_triangle_perimeter():
    t = Triangle(3, 4, 5)
    assert t.perimeter() == 12


def test_triangle_set_sides():
    t = Triangle(3, 4, 5)
    t.set_sides(6, 8, 10)
    assert t.a == 6
    assert t.b == 8
    assert t.c == 10
    assert t.perimeter() == 24


def test_triangle_angles():
    t = Triangle(3, 4, 5)
    assert t.angles() == pytest.approx((36.87, 53.13, 90.0))


def test_triangle_angles_sum():
    t = Triangle(7, 8, 9)
    assert sum(t.angles()) == pytest.approx(180, abs=0.1)


def test_triangle_angles_not_exist(capsys):
    t = Triangle(1, 2, 3)
    assert t.angles() is None
    assert "не существует" in capsys.readouterr().out


def test_equilateral_creation():
    e = Equilateral(4)
    assert isinstance(e, Triangle)
    assert e.a == 4
    assert e.b == 4
    assert e.c == 4


def test_equilateral_perimeter():
    e = Equilateral(4)
    assert e.perimeter() == 12


def test_equilateral_angles():
    e = Equilateral(4)
    assert e.angles() == pytest.approx((60.0, 60.0, 60.0))


def test_equilateral_area():
    e = Equilateral(4)
    assert e.area == pytest.approx(4 * math.sqrt(3))
    assert e.calc_area() == pytest.approx(4 * math.sqrt(3))


def test_equilateral_set_sides():
    e = Equilateral(4)
    e.set_sides(10)
    assert e.a == 10
    assert e.b == 10
    assert e.c == 10
    assert e.perimeter() == 30
    assert e.area == pytest.approx(25 * math.sqrt(3))
