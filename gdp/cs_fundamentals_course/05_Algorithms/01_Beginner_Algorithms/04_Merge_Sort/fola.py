
def count(n): #5
    print(n) #5
    if n == 0:
        return #
    count(n-1)

count(5)




def l_count(n):
    for i in range(n):
        if n == 0:
            return 
        print(n)
        n -= 1 
l_count(5)        
