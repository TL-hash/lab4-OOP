#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 1 (Вариант 7).

Составить программу с использованием иерархии классов. В раздел программы, начинающийся после инструкции
if __name__ == '__main__': добавить код, демонстрирующий возможности
разработанных классов.

Создать класс Triangle с полями-сторонами. Определить методы изменения сторон,
вычисления углов, вычисления периметра. Создать производный класс Equilateral
(равносторонний), имеющий поле площади. Определить метод вычисления площади.
"""

import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def set_sides(self, a, b, c):
        #изменение сторон
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def angles(self):
        #углы в градусах
        if self.a + self.b <= self.c or self.a + self.c <= self.b \
                or self.b + self.c <= self.a:
            print("Треугольник с такими сторонами не существует")
            return None

        cos_a = (self.b ** 2 + self.c ** 2 - self.a ** 2) / (2 * self.b * self.c)
        cos_b = (self.a ** 2 + self.c ** 2 - self.b ** 2) / (2 * self.a * self.c)
        cos_c = (self.a ** 2 + self.b ** 2 - self.c ** 2) / (2 * self.a * self.b)

        angle_a = round(math.degrees(math.acos(cos_a)), 2)
        angle_b = round(math.degrees(math.acos(cos_b)), 2)
        angle_c = round(math.degrees(math.acos(cos_c)), 2)
        return angle_a, angle_b, angle_c


class Equilateral(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
        self.area = 0
        self.calc_area()

    def set_sides(self, side):
        super().set_sides(side, side, side)
        self.calc_area()

    def calc_area(self):
        self.area = self.a ** 2 * math.sqrt(3) / 4
        return self.area


if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    print("Периметр:", t.perimeter())
    print("Углы:", t.angles())

    t.set_sides(6, 8, 10)
    print("Стороны:", t.a, t.b, t.c)
    print("Периметр:", t.perimeter())
    print("Углы:", t.angles())

    e = Equilateral(4)
    print("Стороны:", e.a, e.b, e.c)
    print("Периметр:", e.perimeter())
    print("Углы:", e.angles())
    print("Площадь:", round(e.calc_area(), 2))

    e.set_sides(10)
    print("Стороны:", e.a, e.b, e.c)
    print("Периметр:", e.perimeter())
    print("Площадь (поле area):", round(e.area, 2))