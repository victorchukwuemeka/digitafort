
#TODO    
# eng 
# 
class Eng:
    def __init__(self, hp, f_ty):
        self.hp = hp
        self.f_ty = f_ty
        
    def start(self):
        print("we just started our eng")
        return (f"start engine with {self.hp} and {self.f_ty}")

class Wheel:
    def __init__(self, size):
        self.size = size   

#
class Car: 
    def __init__(self,brand, color,eng, wheel_size):
        self.brand = brand
        self.color = color 
        self.eng = eng 
        self.wheel = [Wheel(wheel_size)] * 4 

    def drive(self):
        eng_status  = self.eng.start()
        return f"our {self.brand} is driving {eng_status}"
    



v8 = Eng(450, "petrol")
mustang = Car("Ford Mustang","black",v8, 18)

print(mustang.drive())
# Ford Mustang is driving. Engine started (450hp, petrol)
print(mustang.eng.f_ty)  # petrol
































"""
class Dog:
    pop = 0   # class attr 

    def __init__(self, name, age):  #instance attr 
        self.name  = name 
        self.age = age 
        Dog.pop +=1 

    def _speak():
"""     
         








#bingo = Dog("bingo", 15)
#hehe = Dog("hehe",7)

#p   =  Dog.pop
#print(p)
