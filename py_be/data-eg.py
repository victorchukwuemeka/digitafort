
"""
bytes_data = b"hello"
#print(bytes_data[2])
w  = b"wop"


bytes_data_array = bytearray(b"world")

bytes_data_array[0] = 87


memory_data = memoryview(bytes_data_array)

print(f"the is memory data{memory_data} ")

"""


tasks = ["cooking",'EATING',"RUNNING"]
tasks.append("sleeping")

tasks[0] = "dancing"

tasks.remove("dancing")


my_t = (5,6,6,6,6,"good")
my_t2 = ("victor",)
my_t3 = ("victor")
     
m_t =   (1,2,[3,4,5])
m_t[2][1] = 8

a,b,c = m_t 

num = (2,4,5,6,8)
first, *second , last = num

def alice_data():
    return "alice" , 30 , "alice@gmail.com"
name, age, email = alice_data()


import sys 

my_list = [2,4,6,8]
my_turple = (2,4,6,8)

#print(sys.getsizeof(my_list))
#print(sys.getsizeof(my_turple))


from collections import namedtuple


Point  = namedtuple('Point',['x','y','z'])

p1 = Point(x=10, y=20, z=30)
p2 = Point(5,15,25)


user_profile = {
    "name" : "victor",
    "emal" : "victor@gail.com",
    "is_active": True,
    "role" : ["admin","normal user "]
}

user_profile["state"]= "Lagos state"
user_profile["is_active"] = False
print(user_profile)



my_new_dict = dict(name="alice",age=45)
#print(type(my_new_dict))



#print(type(a))
#print(f" Turple:{type(my_t2)} and  String:{type(my_t3)}")


#Todo 
#we want tconvert number to an integer 
# and a proper error handling 
try:
    #var for the string 
    num_str = "abc"
    num = int(num_str)
    print(num)

except ValueError:
    print(f"integer conversion failed")