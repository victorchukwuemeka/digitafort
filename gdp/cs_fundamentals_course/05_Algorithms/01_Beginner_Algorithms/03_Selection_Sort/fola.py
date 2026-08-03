arr = [64,25,12,22,11]


def sel_sort(arr):
    #firts gret the num
    num = len(arr)
    #loop through list 
    for i in range(0, num):
        print(i)
        min_idx = i
        for j in range(i +1 , num):
            #print(arr[min_idx])
            #print(arr[j])
            if arr[min_idx] > arr[j]:
                min_idx = j
            temp = arr[min_idx]
            arr[min_idx] = arr[i]
            arr[i] = temp
            temp = None
    return arr

print(sel_sort(arr))
