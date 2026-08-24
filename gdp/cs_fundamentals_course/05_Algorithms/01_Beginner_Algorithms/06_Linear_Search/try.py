#lst = [3,5,9,11,15,18]

#tar  = 11 

# sentinel_search 


# -> last position is going be replaced -> with target  




nums = [90,6,10,20,25,30,35,200]
tar  = 30 

def r_c_s(nums, tar , idx=0):
        #print(idx) -> output 2
        # len(nums)  -> 8
        #  if 2 >= 8 
        if idx >= len(nums):
            return -1
        #arr[idx] ->  6 
        #tar -> 30 
        # if  6 != 30 true 
        #nums-> list 
        # 30
        # idx -> 2 

        
        if nums[idx] != tar:
            return r_c_s(nums,tar, idx+1)
        return -1 






"""
def sentinel_search(arr, target):
    nums = len(arr)   # print(nums) output -> 6 
    last_idx  = nums-1  # print(last_idx) output -> 5 

    arr[last_idx] =  target #print(arr[last_idx])  output ->11
    
    i = 0   
    while arr[i] != target :  #->  true or false 
        i += 1 
    
    last_e  = arr[last_idx] 
    print(f"Our last index {last_e}")
    print(f"Our index {i}")

    if i < last_idx or arr[last_idx] == target:
       return arr[i]
    return -1


lst = [6,23,7,8,1,99,45,100]
tar = 200

ss = sentinel_search(lst,tar)
print(ss) 

def  add(a,b)->int:
    if a != 0 and b != 0:
        return a + b 
    return -1  

added = add(5,9)
print(added)

"""



#def sentinel_search(arr, target):
    #n = len(arr)
    #last = arr[n - 1]

    # Place sentinel
    #new_p = arr[n - 1] = target
    
    #print(new_p)

    
    #i = 0
    #while arr[i] != target:
    #    i += 1

    # Restore original last element
    #arr[n - 1] = last

    #if i < n - 1 or arr[n - 1] == target:
        #return i
    #return -1



