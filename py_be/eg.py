#def add(a,b):
#    return a + b

#print(add(30,8))
#def describe_pet(animal_type, pet_name):
#    print(f"our animal type is  {animal_type}  and the name is  {pet_name}")


#print(describe_pet(pet_name="bingo", animal_type="dog"))

#def sum_all(*num):
#    total = 0
#    for i in num:
#        total += i
#    return total


#print(sum_all(3,4,2,5))




#def add(a,b)->int:
#    return a + b

#print(add(36, 8))

#|keyword| args |expre
#add_lam = lambda a,b:a+b
# print(add_lam(5,5))

# is_even = lambda x:x % 2 == 0
# print(f"is it even{is_even(9)}")
# print(f"is it even{is_even(10)}")



"""
students  = [("alice",89), ("bob",76),("charlie", 90)]

student_grade  = sorted(students, key=lambda student:student[1])
print(student_grade)

empls = [
    {'name':'ebuka', 'age':"90"},
    {'name':'mane', 'age':'47'},
    {'name': "bobby", "age":"50"}
]

empls_age  = sorted(empls, key=lambda empl:empl['name'])
print(empls_age)


num = [1,2,3,4,5]
print(list(map(lambda x:x**2, num)))


"""

#for obj  in objs:
    #print(obj)





import sqlite3
import os 

DB = 'eg.db'


if os.path.exists(DB):
    os.remove(DB)
    #print("done")


conn = sqlite3.connect(DB)

cur  = conn.cursor()


que = """ CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY , name TEXT NOT  NULL , email TEXT NOT NULL)"""

cur.execute(que)




users_to_insert = [
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com")
]

cur.executemany("INSERT INTO users(name,email) VALUES(?,?)",users_to_insert)




cur.execute("SELECT * FROM users")
all_user  = cur.fetchall()
for user in  all_user:
    print(user)


cur.execute("SELECT *  FROM users WHERE name = ?", ("Bob",))

bob = cur.fetchone()
if bob:
    print(f"yeah he exist")
else:
    print("NAH ")


update_query = "UPDATE users SET email = ? WHERE name = ?"
cur.execute(update_query,("bob.whatevergmail.com","Bob"))


d = "DELETE FROM users WHERE name =?"
cur.execute(d,("Bob",))

conn.commit()

conn.close()