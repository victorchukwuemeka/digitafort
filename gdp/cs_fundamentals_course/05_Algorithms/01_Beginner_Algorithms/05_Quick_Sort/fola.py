
#  wrapper
def q_sort(arr):
    _q_s_re(arr, 0,  len(arr)-1)


    
    return arr 

def _q_s_re(arr, low:int, high:int):
    return  arr 



# todo 
# get our array []
#i = 0 
# pivot  = arr[-1]
#  pointer j  loop arr with j 
#  compare the p > i 
# 2 <= 4  





def _par(arr, low, high):
    i = len(low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i  = i + 1  
            arr[j],arr[i]  = arr[i], arr[j]
                
