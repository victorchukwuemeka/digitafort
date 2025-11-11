

my_turple = (1,"vic","Nig", "4")
print(f"try turple:{my_turple}") 


a_turple = ('google',)
n_turple = ('google')

print(f"turple :{a_turple}, type:{type(a_turple)}")
print(f"not one :{n_turple}  type: {type(n_turple)}")


packed_turple = 10,20,30, "two"
print(f"packed :{type(packed_turple)}")

mut_t = (1,2,3,[4,5,6])
print(f"mut : {mut_t}")
mut_t[3][1] = 7
print(f"muted :{mut_t}")

a,b,c,d = packed_turple
f,x, y,z  = mut_t
z0 = z[0]
print(f"the l 0 is :{z0}") 
print(f"each turple {a},{b}, {c} ,{d}")


grade = (10,30,80,50,21)
first, *second,  last = grade
print(f"middle of the middle is :{second[1]}")
print(f"first:{first}, second:{second}, last:{last}")
print(f"index of 10 is {grade.index(30)} while it appear {grade.count(30)} times")
