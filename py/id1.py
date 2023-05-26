#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально задействовав
имеющиеся в Python средства перегрузки операторов.
Вариант 29(9)
9. Поле first — целое положительное число, часы; поле second — целое положительное
число, минуты. Реализовать метод minutes() — приведение времени в минуты.
"""


class MyTime:
    def __init__(self, first=0, second=0):
        if isinstance(first, int) and isinstance(second, int) and first >= 0 and second >= 0:
            self.first = first
            self.second = second
        else:
            raise ValueError

    def __str__(self):
        return f"First (hours): {self.first}\nSecond (minutes): {self.second}"

    def __add__(self, other):
        if isinstance(other, MyTime):
            total_minutes = self.first * 60 + self.second + other.first * 60 + other.second
            hours = total_minutes // 60
            minutes = total_minutes % 60
            return MyTime(hours, minutes)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, MyTime):
            total_minutes = self.first * 60 + self.second - (other.first * 60 + other.second)
            if total_minutes >= 0:
                hours = total_minutes // 60
                minutes = total_minutes % 60
                return MyTime(hours, minutes)
            else:
                raise ValueError("Resulting time cannot be negative")
        else:
            raise TypeError("Unsupported operand type for -")

    def read(self):
        try:
            self.first = int(input("Enter hours: "))
            self.second = int(input("Enter minutes: "))
        except:
            print("Error")

    def display(self):
        print(f"First (hours): {self.first}")
        print(f"Second (minutes): {self.second}")

    def minutes(self):
        print(f"Time in minutes: {self.first * 60 + self.second}")


def make_MyTime(first, second):
    return MyTime(first, second)


if __name__ == '__main__':
    time1 = MyTime(3, 45)
    time1.display()
    time1.minutes()
    time2 = MyTime(1, 30)
    time3 = time1 + time2
    time3.display()
    time4 = time1 - time2
    time4.display()
