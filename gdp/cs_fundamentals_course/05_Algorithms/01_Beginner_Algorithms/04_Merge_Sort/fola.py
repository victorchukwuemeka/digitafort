def m_sort(arr):
    # get the len of our arr
    #  mid  of our arr

    num = len(arr)
    if num > 1:
        mid = num//2
        L = arr[:mid]
        R = arr[mid:]

        m_sort(L)
        m_sort(R)

        i=j=k= 0

        while 



[38, 27, 43, 3, 9, 82, 10]

f
num = 7 
7 > 1 :
7 // 2 
l = [38,27,43]
r = [3,9,82,10]

f1
m_sort(l)
num = 3 
3 > 1
3//2 
l = [38]

f1.1
m_sort(l)
num = 1
1  >1 

f1.2
m_sort(lr)
num = 2
2 > 1
2 // 2
lr = [27]






[38] [27] [43]
[3] [9] [82] [10]

f1
m_sort(r)
num = 4
4 > 1
4//2
r = [3, 9]

f1.1
m_sort(r)
num = 2
2  >1
2 // 2
rl = [3]



f1.2
m_sort(lr)
num = 2
2 > 1
2 // 2
lr = [27]


