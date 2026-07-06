"""
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand  = brand

    def describe(self):
        return f"A {self.color} {self.brand}"


t = Car("red","tesla")
j = Car("white","Jeep")

print(t.describe())
print(j.describe())


class Employee:
    c = "techC"
    epc  = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.epc += 1

salah = Employee("salah",200)
mane = Employee("mane",200)
bobbi = Employee("bobbi",200)

print(Employee.epc)

"""


class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def get_p(cls):
        return cls.population

    @classmethod
    def birth_age(cls, name, birth_year):
        import datetime

        age = datetime.date.today().year - birth_year
        return cls(name, age)


t = Person("Tunde", 90)
s = Person.birth_age("salah", 1995)

print(Person.get_p())
print(s.age)


people = 10
name = "grace"
age = 40
date_of_birth = 1986

name = "destiny"
age = 30
des_date_of_birth = 1996

num_1 = 89
num_2 = 43
num_3 = 0
num_3 = num_1 + num_2


def add(a, b):
    return a + b


add(89, 43)


import requests

res = requests.get("sjjsjsj")


class Perso:
    def __init__(self, name, age, date_of_birth):
        self.name = name
        self.age = age
        self.date_of_birth = date_of_birth


g = Perso("messi", 39, 1987)

g = Perso("jjjj", 39, 1987)
