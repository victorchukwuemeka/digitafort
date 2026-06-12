name = "victor"
num = 89
print(f"Name is {name}")

name = "akin"
num = 45 
print(f"Name is {name}")




class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def show(self):
        print(self.name)


Person("sofy", 89)
Person("amad", 90)



class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def b(self):
        print(f"{self.name} breaths air")

    def s(self):
        print(f"{self.name} speak")


class Dog(Animal):
    def __init__(self, name, age,  breed):
        super().__init__(name, age)
        self.breed = breed 

    def s(self):
        print()





    