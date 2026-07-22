
def anything(nums:list):

    l = nums[0]

    for num in nums[1:]:
        if num < l :
            l = num
    return l 


nums  = [8,2,1,7,9,4]

print(anything(nums))


