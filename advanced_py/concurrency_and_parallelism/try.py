import multiprocessing 

# amount , lock , value 
def add_money(amount, lock, value):
    for _ in range(100):
        with lock:
            value.value += amount 


if __name__== "__main__":
    value = mutliprocessing.Value("i",0)
    lock =  multiprocessing.Lock()

    procs = [multiprossing.Process(target=add_money, args=(5,lock,value)) for _ in range(4)]

    for p in procs: 
        p.start()
    for p in procs:
        p.join()






#[4,6,678,03]
     
#jj[1] =  9 

#[4,9,678,03]
