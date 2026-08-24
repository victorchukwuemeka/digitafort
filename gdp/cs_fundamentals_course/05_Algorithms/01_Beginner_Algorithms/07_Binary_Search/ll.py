


def binary(arr, target):
    low = 0
    high = len(arr) -1 

    while low <= high:
        mid  = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else :
            high = mid - 1
    return -1 



def recursive(arr, target, low , high):
    if low > high:
        return -1 
    
    mid = (low + high) // 2 

    if arr[mid] == target:
        return mid 
    elif arr[mid] < target:
        return recursive(arr, target, mid +1, high)
    else :
        return recursive(arr, target, low, mid -1)
    




















"""
def binary_search(arr, target):
    low  = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + high // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            low = mid + 1
        
        else:
            high = mid - 1

    return -1 

"""


""""
def recursive(arr, target ,low,high):
    if low > high:
        return -1
    
    mid =  low + high // 2 

    if arr[mid] == target:
        return mid 
    elif arr[mid] < target:
        return recursive(arr, target, mid + 1 , high)
    else :
        return recursive(arr, target, low, mid -1 )


recursive([10], 10, 0, 0)

"""

