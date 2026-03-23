"""

tasks = ["coooking", "cleaning","sleeping",5]
tasks.append("walking")
tasks.remove()
print(tasks)
"""



"""
t = (1, "hello", 2.14 , "hello")
print(t)
a,b,c,d = t
print(t)


o = 12,13, "victor"
r = type(o)
#print(r)



m = (1,2,[3,4,5])
l = m[2]
l[2] = 8
#print(l)


ls = [1,2,(3,4,5)]
#ls[2][0] = 6
#print(ls)


point = (10,20)

location_data = {
    (40.7128, -74.0060): "New York City",
    (34.0522, -118.2437): "Los Angeles"
}


print(f"Data for {point}: {location_data.get(point, 'Not Found')}")

s_grade = {
    "math":89,
    "Bio" : 90,
    "GNT" : 79
}


for s,g in  s_grade.items():
    print(s,g)



"""

import sys
 
l = [1,2,3,4,5]
t = (1,2,3,4,5)

#print(f"get the list size :{sys.getsizeof(l)}")
#print(f"gte the turple size: {sys.getsizeof(t)}")


"""
from collections import namedtuple

Point = namedtuple('Point',['x','y','z'])

p1 = Point(x=10, y=20, z=30)
p2 = Point(2, 4, 11)



user_profile = {
    "name": "jdoe",
    "email": "jdoe@gmail.com",
    "is_active": True,
    "role" : ['admin', 'client']
}

p = dict(name="jdoe", mail="jdoe@gmail.com")

user_profile["age"] = 45
user_profile["is_active"] = False
del user_profile["age"]



print(user_profile)





company_data = {
    "empl1":{
        "name":"alice",
        "depart":"HR"
    },
    "empl2":{
        "name":"jdoe",
        "depart":"sales"
    }
}
g = company_data["empl2"]["name"]
print(g)


"""


"""
text = "Hello, 世界! 🐍"
encoded_utf8 = text.encode('utf-8')
encoded_ascii = text.encode('ascii', errors='ignore')
print(encoded_utf8)      
print(encoded_ascii)     
"""


import jwt 
import datetime


PASS = "password"


payload = {
    'id' : 42,
    'email':"example@gmail.com",
    'age' : 24,
    'name' : "jon doe",
    'iat' : datetime.datetime.utcnow(),
    'exp' : datetime.datetime.utcnow()+ datetime.timedelta(hours=1)
}


t = jwt.encode(payload, PASS, algorithm="HS256")


print(t)