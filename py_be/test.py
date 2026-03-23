"""
# Python with Databases: Interacting with SQLite using `sqlite3`

This file provides a guide to using Python's built-in `sqlite3` module to work
with SQLite databases. SQLite is a lightweight, serverless, file-based database,
which makes it incredibly easy to get started with databases in Python.
"""

#import sqlite3
#import os


#DB_FILE = "example.db"


#todo
# check if file exist 
# clean the old db 
#if os.path.exists(DB_FILE):
#    os.remove(DB_FILE)

#erro check 
#connect 
#try:
#    connect_db = sqlite3.connect(DB_FILE)
#except sqlite3.DatabaseError as e:
#    print(f"failed{e}")


#name = int(input("Your Age :"))
#print(name)

#import tkinter as tk 

#root = tk.Tk()
#root.title(" My app")


#root.mainloop()



#string
#int
#float
#bool


#kkkkkkkkkkk
"""
kkkkkkkkkkk
"""

#create 2 a var 
# add the value 
# substract them 
# **
# * 


#a = 8 # attend classes
#b = 3 # read your books
#c = 6 # don't attend 
#d = 4

#passing  =  (a > 3) or (c < d)
#print(passing)


#name = 40 
#name -= name 


#if you came to class -> if you came with your system   -> learn 
#else ->dont learn 

a = 2
b = 3
c,d = a,b 




#position , apple = en(0,apple)

#0, apple
#en(0,apple ) = [
#  0 : apple
# ]
#       0       1         2


#





          
fruits = ["apple","orange"]
fruits.append("mango")
fruits.append(9.333)
fruits[2] = "banana"
fruits.remove(9.333)
fruits.append("apple")



#print(f"this are the item: {item}", type(item))

#                0,1,2, 3
mutable_tuple = (1,2,3, [4,5,6])
mutable_tuple[3][0] = 89

number =  (1,2,3,3,4,5,6)
first , *second, last  = number 
#print(first, *second, last)



#def get_more_value():
#    return "alice", 30, "example@gmail.com"


#name, age , mail = get_more_value()
#print(name,age,mail)



#location  = {
#    (40.7128, -74.0060): "New York City",
#    (34.0522, -118.2437): "Los Angeles"
#}

#import sys


#num_l = [1,2,3,4,5]
#print("List size in bytes :",sys.getsizeof(num_l))
#num_t = (1,2,3,4,5)
#print("Turple Size i Bytes: ", sys.getsizeof(num_t))

#from collections import namedtuple

#Point = namedtuple('Point',['x','y','z'])


#anything = { "name": "victor", "age" : 92,  "location":"UK" }

#print(anything['name'])




user_profile = {
    "name" : "salah",
    "email" : "example@gamil.com",
    "is_active": True,
    "roles" : ["admin", "users"]
}
#print(user_profile["email"])
user_profile["is_active"] = False

user_profile.update({"school": "UNN"})
#print(f"Before pop :",user_profile)
user_profile.popitem()
user_profile.clear()
#print(user_profile)


#dictionary
"""
student_grade = {
    "Bio" : 90,
    "MTH" : 76,
    "BCH" : 67
}

for subject, grade  in student_grade.items() :
    print(f"Student  Subjects and Grade: {subject},{grade}")


company_data = {
    "employee" :{
        "empl001" : { "name" : "alice", "age": 90},
        "emploo2" : { "name" : "salah", "age": 60}
    },

    "location" : ['lagos', "Nigeria"]
}
"""

# set eg
#lan_tag = ["python", "php", "python", "rust","java", "c"]

#unique_lan = set(lan_tag)

#print(f"Lan List :", lan_tag)
#print(f"The Set  :", unique_lan)

#set_a = {1,2,3,4}
#set_b = {3,4,5,6}

#inter_set = set_b.difference(set_a)
#print(f"the union of {set_a} and {set_b} is {uni_set}")











"""
good_day = "Good Morning"

print(good_day)
"""





#greeting 
"""
def good_night(): #good nigth 
    good = "Good evening"
    print(good)


good_night()


def welcome_message():
    print("Welcome to functions")


welcome_message()


def add(a,b=2)->int:
    return  a + b # ..............
    print("done")


num = add(2)
print(num)



def greet_user(name):
    message = "Good Morning"
    print(f"{message}, {name}")

greet_user("victor")
"""


"""

def add(a,b):
    c = a + b
    print(c)

add(3,4)




def describe_pet(ani_type, pet_name):

    print({ani_type},{pet_name})

describe_pet(pet_name="dog", ani_type="mammals")





def numbers(*nums):
    print(nums)


numbers(1,7,66,6)

numbers(1,2,3,4)


"""


"""
print(" Hello , Python!")
"""



"""
def add(a,b):
    return a + b 
    


add_lambda = lambda a,b:a + b


is_even = lambda x : x % 2 == 0 


print(add(4,4))
print(add_lambda(4,2))

print(is_even(8))



students = [("alice", 35),("bob", 23), ("fred", 25)]

sorted_by_grade =sorted(students, key=lambda student: student[1])

print(sorted_by_grade)
"""




girl = "fisa"
num   = 97
amount = 5.00
boy = True
#print(type(girl))
#print var


""" 
fhfhffhhfhfhf
fffhfhfhfhhfhf
fhfhfhfhfhfhsss
"""




name = "victor"

greet = "good morning"


def greeting(name):
    print(f"Hello:",name)


#greeting("dami")



#name = input("Your Name:")
#print(f"hi:", name)

#numb = int(input("add phone number :"))
#print(numb)

"""
first_name = "chukwuemeka"
last_name = "victor"
print({first_name + last_name})
"""



#math_expr =lambda a,b: a + b 
#print(math_expr(5,7))



#def add(a,b):
#    return a +b 



#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#even_num = filter(lambda  number)
#print(f"Even : {even_num}")


#      key    arg    
#age = lambda age:"adult" if age >= 18 else "Minor"
#print("Your Age :", age(21))


#fruits = ["apple", "orange","banana"]

#for fruit in fruits:
#    print(f"I love : {fruits}")





"""
def guess_g(secret_num):
    guess = 10
    while guess != secret_num:
        print(f"{secret_num} don't match the")
        return 
    print(f"You Won {guess} matches the {secret_num}")



num = int(input("Your Game Number:"))
#print(num)
guess_g(num)

"""
"""
for i in range(5):
    print(i)
print()
"""






"""
try:
    with open('victor.txt', 'w') as victor:
        victor.write("jfjfjfj kfkkf lflf. \n")
        victor.write("nothing else. \n")
        victor.write("alalalalala. \n")
    print("it worked ")

except IOError as e:
    print(f"{e} occurred")

"""




"""
my_new_file = open("victor.txt", "a")

data_inputed  = my_new_file.write(" anything is okay . \n") 

if data_inputed :
    print("We added a text to the file")

"""


#= open("victor.txt", 'w')
#my_new_file.write("hhhhhfkkf . \n")






import sqlite3
import os 


DB_FILE = "new_db.db"

"""
clearing of the db 
"""

if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print(f"cleared the old data in {DB_FILE}")




"""
db connections , we stated 
"""
print(" THe db connections \n")
conn = sqlite3.connect(DB_FILE)
print("db created ")


cur = conn.cursor()

create_tb_q = """
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY,
name  TEXT NOT NULL,
email TEXT NOT NULL UNIQUE
)
"""

cur.execute(create_tb_q)
print("EXecuted")



cur.execute("INSERT INTO users (name,email) VALUES (?, ?)", ('alice', 'alice@gmail.com'))


many_users = [
    ("victor","vitor@gmail.com"),
    ("cine", "cine@gmail.com")
]

cur.executemany("INSERT INTO users(name , email) VALUES (?,?)", many_users)

conn.commit()


update_query = "UPDATE users SET email= ? WHERE name = ?"

cur.execute(update_query, ("alice.whatever@mail.come", "alice"))
conn.commit()

delete_query = "DELETE  FROM users WHERE name = ?"
cur.execute(delete_query,("victor",))
conn.commit()


cur.execute("SELECT * FROM users")

all_users = cur.fetchall()
for user in all_users:
    print(f"  ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")


