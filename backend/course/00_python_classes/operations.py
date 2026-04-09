#imp
a = 32
b = 40 
c = a + b 

d = 45
f = 6
q = d -f 


#func
def add(a,b):
    return a +b 
def subtt(d,f):
    return d -f


#class
class Operations:
    def add(self, a,b):
        return a + b
    def subttt(self, d,f):
        return d - f 
    



#imp
print(f"for addition:{c}")
print(f"for sub: {q}")


#fp 
print(add(17,35))
print(subtt(70,35))

#class
add_sub =  Operations()
print(add_sub.add(9,8))

sub_add = Operations()
print(sub_add.add(8,4))

#print(Operations.add(12,2))


class Dog:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age 
    

rex = Dog("rex","red",6)
rex_name  = rex.name = "john"
rex_name = "cena"
#print(rex_name)
print(rex.name)

#print(rex_name = "john")
#rex_name = "john"
#print(rex.name)