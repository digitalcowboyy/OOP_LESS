# Практические задачи с сайта:
# https://w3resource.com/python-exercises/oop/index.php
# Задачи 1-4,8,11


# 1. Circle Class for Area and Perimeter
# Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        """Площадь круга"""
        return 3.14 * self.radius ** 2

    def perimetr(self):
        """Длина окружности"""
        return 2 * 3.14 * self.radius


# a = Circle(5)
# print(a.area())
# print(a.perimetr())


# 2. Person Class with Age Calculation
# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import date


class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def __str__(self):
        return f"{self.name} из страны {self.country}, его возраст {self.age}"

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age


# pers1 = Person("Demid", "Russia", date(2000, 12, 25))
# pers2 = Person("Valera", "Russia", date(2000, 10, 6))
# print(pers1)
# print(pers2)


# 3. Calculator Class for Basic Arithmetic Operations
# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return self.number / other.number

# x = Calculator(10)
# y = Calculator(5)
# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)

