
temp = 21 
if temp < 20:
    print("cold day ")
else:
    print("hot day")

sc = 85

if sc > 90 :
    print("grade  a ")
elif sc > 75 :
    print("grade B ")
elif sc > 65 :
    print("grade C")
elif sc >  55 :
    print("grade D")
elif sc < 55 :
    print(" grade F ")


age = 18 
lc = True 

if age >= 18:
    if lc == True :
        print("drive")
    else: 
        print("you are old enough but no lc  ")
else:
    print("not old enough")




try:
    num_str = "abc"
    num = int(num_str)
    print(num)
except ValueError:
    print(f"string did not convert {num_str}")




fruits = ["appl","ban","cherry"]
for f in fruits:
    print(f"i like {f}")


for c in "python":
    print(c)  


for i in range(1000):
    print(i)



for i , v in enumerate(fruits):
    print(i,v)


c = 0
while c < 3:
    print(c)
    c += 1 


i = 0 

while True:
    print(i)
    if i >=  100:
        break
    i += 1
    




a = 10 
b = 50 
c = a + b 

def add(a,b):
    return a +b 

add(47,98)



