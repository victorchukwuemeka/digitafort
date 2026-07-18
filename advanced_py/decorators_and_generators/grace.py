
def get_num_list(num):
    num_list = []
    for n in range(num):
        num_list.append(n *1)
    return num_list 

num = 10000000000
#num_index  = get_num_list(num)
#print(num_index)


def get_num_gen(num):
    for n in range(num):
        yield n * 1 
num = 100000000000

num_gen  = get_num_gen(num)
for n in num_gen:
    print(n)
    
print(next(num_gen))
print(next(num_gen))


def countdown(n):
    while n > 0:
        yield n 
        n -=  1


gen2 = countdown(3)
print(next(gen2))
print(next(gen2))
print(next(gen2))

