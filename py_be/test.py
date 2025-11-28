"""
data = [9,"four",56,"football",99,88,4,"good","bad","global"]



number_list = []
string_list = []


for d in data:
    if type(d) == int:
        number_list = number_list + [d]
    else:
        string_list = string_list + [d]
print(number_list)
print(string_list)




#num = [1,2,3,4,5,6,7]
#count = len(num)


count = 10
while count > 1 :
    print(count)
    count = count - 1
    continue




for i in range(5):
    print(i)
    break


num = [2,4,6,8,10]

for i in num:
    print(i)
    if i == 6:
        break

age = int(input("Your age7- :"))
print(age)
"""


boy = "victor"
print(boy)


"""
print("Using `break` to stop at the number 2:")
for i in range(5):
    if i == 2:
        break  # Stop the loop when i is 2
    print(i)
print()

# `continue`: Skips the rest of the current iteration and moves to the next one.
print("Using `continue` to skip the number 2:")
for i in range(5):
    if i == 2:
        continue  # Skip this iteration when i is 2
    print(i)
print()

print("End of Loops Explanation")
"""



"""
print("Example 2: A simple guessing game")
secret_number = 7
guess = 0
while guess != secret_number:
    print(f"You guessed {guess}. That's not it!")
    # In a real game, you'd ask for a new guess. Here we'll just increment.
    guess += 1
print(f"You guessed {guess}. You got it! It was {secret_number}.")
print()

89
"""

"""
secret_number = 9
guess = 0


while guess != secret_number:
    guess = int(input("enter your guess: "))
    if guess != secret_number:
        print(f"{guess} is the wrong guess do better ")
    elif guess == secret_number:
        print(f"{guess} is the wright one")
print(f"the secret number is {secret_number}")
"""


""""
def add(a :int, b:int):#ab are para
    num =  a + b 
    print(num)

add(4, 4)
"""


""""
def is_even(num):
    if num  % 2 == 0:
        return True
    else:
        return False
 


result = is_even(5)
print(result)
"""

def hello():
    return " Good girl"

hello()




def largest_in_list(numbers):
    if not numbers:  
        return None
    
    largest = numbers[0]
    #print(largest)
    for num in numbers:
        if num > largest:
            largest = num
    return largest


big_list = [10, 25, 14, 99, 3, 87, 200, 150]



















largest_in_list(big_list)


def add(a,b):
    return a+b

add(4,8)


##print(largest_in_list(big_list))  


""""
def addl(a,b):
    return a + b 


def add(a,b):
    sum = a + b
    return sum
"""

#lambda argument: expression 

#add = lambda a,b: a + b
#print(add(2,2))





#is_even = lambda x: x % 2 == 0

#is_even = lambda x: x % 2 == 0


#age_check  = lambda age: "An Adult" if age >= 18 else "a minor"

#print(age_check(15))

##lambda age: "An adult" if age >= 18 else "a minor"

#age_check = lambda age:"An Adult" if age >= 18 else "a minor"
#print(f"your are {age_check(23)} ")
#good = lambda a,b : a + b

#print({good(2,2)})

"""
employees = [
    {'name': 'John', 'age': 35},
    {'name': 'Jane', 'age': 28},
    {'name': 'Dave', 'age': 42}
]

# Sort by age
sorted_by_age = sorted(employees, key=lambda employee: employee['age'])
print(f"Employees sorted by age: {sorted_by_age}")
print()

"""

people = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 40},
    {"name": "Eve", "age": 20},
    {"name": "Mike", "age": 35}
    ]
people_sorted = sorted(people, key=lambda x: x['age'])
print(people_sorted)