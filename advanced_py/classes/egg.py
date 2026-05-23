class Person:
    population = 0

    def __init__(self,name, age):
        self.name = name 
        self.age = age 
        Person.population += 1

    @classmethod
    def get_population(cls):
        return cls.population 
    
    @classmethod
    def from_birth_year_get_age(cls,name , birth_year):
        import datetime
        age  = datetime.date.today().year - birth_year
        return cls(name, age)
    

