"""
try:
    s = "abc"
    num = int(s)
    print(num)
except ValueError:
    print("convertion Error")




for i in range(5):
    print(i)



count = 0
while count < 3:
    print(f"our count {count}")
    count +=1 

"""


"999999999999"


#your_amount = float(input("say your amount: "))

#print(your_amount)

"""
num_str = input("your input: ")
#print(num_str)
try:
    num_list  = num_str.split()
    n1 = num_list[0]
    n2 = num_list[1]

    print(f"first: {n1} and second :{n2}")
except(ValueError, IndexError):
    print("Error")

"""


#def add(a, b):
#    return a + b

#l = list(map(add, [2, 3], [4, 5]))
#print(l)  

#add()

#lambda argument expression
#lambda a,b: a+b 

#lambda age: "Adult"  if age >= 18 else "Minor"



#val1 = 6  
#val2 = 2


#print(f"Bitwise AND ({val1} & {val2}): {val1 & val2}")




"""

students =  [("alice",92), ("bob",85), ("charlie", 95)]
sorted_by_grade  = sorted(students, key=lambda student:student[1], reverse=True)
print(f"the student grade {sorted_by_grade}")

emplys  = [
    {"name": "John", 'age':35},
    {"name" : 'alice ', 'age': 30},
    {"name ": 'dave', 'age':14}
]


print(sorted(emplys, key=lambda empl : empl['age']))




numbs = [2,4,6,8,10]

s_nubms = map(lambda x:x**2 , numbs)

print(list(s_nubms))




numbs = [1,2,3,4,5,6,7,8,9,10]
filter(lambda x:x % 2 == 0, numbs)


"""



with open("file_back_end.txt", 'w') as file:
    file.write("hello word. \n")
    file.write(" a new file \n")
    file.write("nothing much \n")
print("done")

with open("file_back_end.txt","r") as file :
    content = file.readlines()
    for i in content:
        print(i)
print("done reading")

with open("file_back_end.txt","a") as file:
    file.write("whatever man . \n")
print("append is working ")