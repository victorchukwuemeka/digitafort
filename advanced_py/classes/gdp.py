#primate to have properties that we can inherit 
class Homoerectus:
    #construct -> name, color 
    def __init__(self , name, color):
        self.name = name 
        self.color = color 

    def run(self):
        return  f"Runs slowly"

    def eat(self):
        return f"eats fruits"


class Human(Homoerectus):
    def __init__(self, name,age,race,color):
        super().__init__(name, color)
        self.race = race
        self.age = age 

    def run(self):
        return f"{self.name} at  {self.age} runs fast" 

    def think(self):
        return f"{self.name} thinks "


class Ape(Homoerectus):
    #def __init__(self, size):
     #   self.size = size 

    def strong(self):
        return f"very strong"


#man = Human("bob",34,"negro","black")
#ape = Ape("African Ape","black")


class Cry:
    def crying(self):
        return f"babies cry alot"

class Sleep:
    def sleeping(self):
        return f"babies sleep alot "

    
class Baby(Sleep, Cry, Homoerectus):
    def eat(self):
        return f"babies always eat "



newbaby = Baby("newbaby",1)
eating = newbaby.eat()
crying = newbaby.crying()
sleeping = newbaby.sleeping()
baby = [eating,crying,sleeping] 
print(baby)


