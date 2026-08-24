arr = [2,2,7,5,9,7,8,8,12,2,19]


def count_occurrences (lists,target):
    count = 0
    for number in lists:
        if number == target:
            count += 1
    return count




count_occurrences(arr, 8)


def already_found (repeated, target):
    for number in repeated:
        if number == target:
            return True
    return False







def find_repeated_numbers (lists):
    repeated = []
    
    for number in lists:
        occurrences = count_occurrences(lists, number)
        if occurrences > 1 :
            if already_found(repeated, number) == False:
                repeated.append(number)
                print(number, "occured", occurrences, "times")

find_repeated_numbers(lists)
    














# linear search ->  with early exit  
#  linear ->  line -> line by line      searchingfor something line by line 
# [6,7,1,3,2,4,5,6,7]
# var ->    first elemtent is min = 6
#    for sth in the lst ->    if  sth <  min ->  true ->    min <-sth 

"""
def fmin(arr):
    min = arr[0]
    for index in range(len(arr)):
        #print(arr[index])
        #print(f"{min}-----")
        if arr[index] < min:
            min  = arr[index] 
    return min 

lst = [5,3,2,5,6,8]  
print(fmin(lst))
"""


"""
def add(x,y):
    return x + y 



a = 10 
b = 10 
add(a,b)




def l_search_s(tar, lst):
    step_count = 0 
    print(step_count)
    for element in lst:
        step_count += 1
        print(step_count)
        if element == tar:
            print(f" our search result is  {element}:")
            return element 
        if  element >= tar:
            print(f"{element}  is greater than {tar}")
        return -1 
    print(step_count)
    return -1 


sorted_list = [5, 10, 15, 20, 25]
result = l_search_s(9,sorted_list)
print(result)
"""







"""
def osearch(tar,y,x, lst):    #basket-> oranges 
    #result = []
    result = []
    x_result = []
    y_result = []
    for i in range(len(lst)):
        if lst[i] == tar:
            result += [i]
        if lst[i] == y:
            y_result += [i]
        if lst[i]  == x:
            x_result += [i]
    total_r = {
        "how many does 7 have": len(x_result),
        "how many does 8 has ": len(y_result),
        "how many does 2 has ": len(result)
    }
    #total_result =  [len(x_result), len(y_result), len(result)] 
    return total_r          

"""


"""
lst = [2,2,7,5,9,7,8,8,12,2,19]
tar = 2
y = 8
x = 7
print(osearch(tar,y,x,lst))
"""



