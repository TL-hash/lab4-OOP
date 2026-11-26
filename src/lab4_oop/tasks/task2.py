#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задание 2 (Вариант 7).

В следующих заданиях требуется реализовать абстрактный базовый класс, определив
в нем абстрактные методы и свойства. Эти методы определяются в производных классах.
Для ввода использовать вспомогательный класс Reader, позволяющий читать данные
с клавиатуры. Для вывода использовать методы __str__ или __repr__.

Вызывающая программа должна продемонстрировать все варианты вызова
переопределенных абстрактных методов. Написать функцию вывода, получающую
параметры базового класса по ссылке и демонстрирующую виртуальный вызов.


7. Создать абстрактный базовый класс Root (корень) с виртуальными методами
вычисления корней и вывода результата на экран. Определить производные классы
Linear (линейное уравнение) и Square (квадратное уравнение) с собственными
методами вычисления корней и вывода на экран.

"""

import math
from abc import ABC, abstractmethod


class Reader:
    #вспомогательный класс для чтения данных с клавиатуры
    def read_float(self, prompt):
        return float(input(prompt))


class Root(ABC):
    def __init__(self):
        self.roots = []

    @abstractmethod
    def calc_roots(self):
        pass

    @abstractmethod
    def show(self):
        pass


class Linear(Root):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def calc_roots(self):
        self.roots = []
        if self.a != 0:
            self.roots.append(-self.b / self.a)

    def show(self):
        print(self)

    def __str__(self):
        text = "Линейное уравнение " + str(self.a) + "x + " + str(self.b) + " = 0: "
        if self.a == 0 and self.b == 0:
            return text + "x - любое число"
        if len(self.roots) == 0:
            return text + "корней нет"
        return text + "x = " + str(round(self.roots[0], 2))


class Square(Root):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def calc_roots(self):
        self.roots = []
        if self.a != 0:
            d = self.b ** 2 - 4 * self.a * self.c
            if d > 0:
                self.roots.append((-self.b - math.sqrt(d)) / (2 * self.a))
                self.roots.append((-self.b + math.sqrt(d)) / (2 * self.a))
            elif d == 0:
                self.roots.append(-self.b / (2 * self.a))

    def show(self):
        print(self)

    def __str__(self):
        text = "Квадратное уравнение " + str(self.a) + "x^2 + " + \
               str(self.b) + "x + " + str(self.c) + " = 0: "
        if self.a == 0:
            return text + "это не квадратное уравнение (a = 0)"
        if len(self.roots) == 0:
            return text + "действительных корней нет"
        if len(self.roots) == 1:
            return text + "x = " + str(round(self.roots[0], 2))
        return text + "x1 = " + str(round(self.roots[0], 2)) + \
               ", x2 = " + str(round(self.roots[1], 2))


def print_result(r):
    r.calc_roots()
    r.show()


if __name__ == '__main__':
    reader = Reader()

    print("Линейное уравнение a*x + b = 0")
    a = reader.read_float("a = ")
    b = reader.read_float("b = ")
    lin = Linear(a, b)

    print("\nКвадратное уравнение a*x^2 + b*x + c = 0")
    a = reader.read_float("a = ")
    b = reader.read_float("b = ")
    c = reader.read_float("c = ")
    sq = Square(a, b, c)

    print("\nВызов методов через объекты производных классов")
    lin.calc_roots()
    lin.show()
    sq.calc_roots()
    sq.show()

    print("\nВызов через функцию, получающую объект базового класса")
    print_result(lin)
    print_result(sq)

    print("\nВызов для списка объектов базового класса")
    equations = [lin, sq]
    for eq in equations:
        print_result(eq)