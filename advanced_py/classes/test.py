"""
class Temp:
    def __init__(self,cel):
        self.cel = cel

    @property 
    def cel(self):
        return self.cel 

    @cel.setter
""" 





"""
class Person:
    population = 0 
    

    def __init__(self, name, age):
        self.name = name 
        self.age = age 
        Person.population += 1

    @classmethod 
    def get_population(cls):
        return cls.population

    @classmethod 
    def f_b_y(cls,name,b_y):
        import datetime
        age = datetime.date.today().year - b_y 
        return cls(name,age)    





salah = Person('salah',98)
mane = Person.f_b_y('mane',1996)


print(f"Person.get_population()")
print(mane.age)
"""
