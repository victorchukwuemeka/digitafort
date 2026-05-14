p_lang = ["python","ada", "c","rust","python"]
unique = set(p_lang)

#print(f"Our list of language: {p_lang}")
#print(f"Our unique set{unique}")



set_a = {1,2,3,4}
set_b = {3,4,5,6}

un = set_a.union(set_b)
#print(f"Set A{set_a} Union Set B{set_b} : UN{un} ")







#your_name = input("what is your name: ")
#print(f"my name is {your_name}")
#print(f"data type of our input by default {type(your_name)}")

#num_1  = int(input("first numbers : "))
#num_2 = int(input("second number: "))
#sum_num = num_1 + num_2
#print(f"Our sum result is {sum_num}")

#while True:
#    try:
#        age = int(input("how old are you :"))
#       if age < 0 :
#            print("age can't be Negative")
#        else:
 #           print(f"your are {age} Years old")
  #          break
  #  except ValueError:
  #      print("Invalid Input check your data")


try:
    num_1 = float(input("first number :"))
    operator = input("enter operators (+,-,*,/): ")
    num_2  = float(input("last number :"))
    print(operator)
    
    if operator == "+":
        result = num_1 + num_2
    elif operator == "-":
        result = num_1 - num_2
    elif operator == "*":
        result = num_1 * num_2
    elif operator == '/':
        if num2 == 0:
            print("Error division by zero not allowed")
            result = Undefined
        else:
            result = num_1 / num_2
    else:
        print("Invalid operator")
        result = "N/A"
    print(result)
    
        
except ValueError:
        print("Invalid input :")
except Exception as e :
        print("Unknown Error")
