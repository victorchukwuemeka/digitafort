import sys

l = [1,2,3,4,5]
t = (1,2,3,4,5)

print(sys.getsizeof(l))
print(sys.getsizeof(t))


up ={
    "name":"john",
    "email":"john@gmail.com",
    "age" : 90,
    "role":["admin","normy"]
}

up['name'] = "salah"
up["is_active"] = True

del up['age'] 
 

print(up)
print("\n--- 3.5. Iterating Through Dictionaries ---")


sg = {
    "mth":90,
    "sc" : 85,
    'eng':78
}


print(sg)

for s,g  in sg.items():
    print(s,g)
