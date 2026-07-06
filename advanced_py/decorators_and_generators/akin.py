

def countdown(n):
    while  n > 0:
        yield n
        n -= 1 
    print("Done")



gen = countdown(5)

for num in gen:
    print(num)


def multiple():
    yield "made a change "
    yield "commited my change "
    yield "push changes "

for m in multiple():
    print(m)





