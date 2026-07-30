
arr = [4,9,2,7,8,3]
def in_sort(arr):
    num = len(arr)
    for i in range(1,num):
        key = arr[i] 
        j = i-1
        #print(arr[j + 1])
        while j>=0 and  key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key 
    return arr  
print(in_sort(arr))
