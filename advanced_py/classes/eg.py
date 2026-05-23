class Dog:
    species ="canis"  #shared
    
    def __init__(self, name, age): #
        self.name = name 
        self.age = age 
        pass




print("==" * 64)
print("Instance attributes")
my_dog = Dog("bingo",  9)
print(my_dog.name, my_dog.age)
print(my_dog.species)


print("===================================================================" * 2)
print("Rex")
your_dog = Dog("rex",8)
print(your_dog.name, your_dog.age)
print(your_dog.species)


print("==================================================================="* 2)
print("New species  Class Attributes")
Dog.species = "canis lupus"
print(my_dog.species)
print(your_dog.species)
print()


print("+" * 30 )
#overide class attribute for a specific object 
print("Overide example")
my_dog.species = "bulldog"
print(f"the specie of my Dog is {my_dog.species}")
print(f"Your dog was not changed it is still {your_dog.species}")




class BankAccount:
    interest_rate = 0.02 
    account_count = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance 
        BankAccount.account_count += 1


my_bank = BankAccount("victor", 100)
your_bank = BankAccount("mercy", 200)
your_schools = BankAccount("your sch", 999)
family_account  = BankAccount("your Family", 500)

#print("*=*"*87)
#print("Our bank accounts ")
#print(BankAccount.interest_rate)
#print(BankAccount.account_count)



class Cat:

    def __init__(self, name,color):
        self.name = name 
        self.color = color
        pass
    
    def name(self):
        return self.name
    
    def color(self):
        return self.color

cat = Cat('new_cat',"grey")
print(cat.color)