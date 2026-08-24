lst  = [5,3,2,5,6,6,9]

def count(lst):
    num = 0
    for l in lst:
        num += 1 
    return num 

def l_search(lst, target):
    for i in range(count(lst)):
        if lst[i] != target:
            i += 1 
    return lst[i]

l_search(lst,9)



