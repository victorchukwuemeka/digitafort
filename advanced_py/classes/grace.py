
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
    def birth_age(cls,name,birth_year):
        import datetime
        age  = datetime.date.today().year - birth_year
        return cls(name,age)



t  = Person("Tunde", 90)
s = Person.birth_age("salah", 1995)

print(Person.get_p())
print(s.age)



