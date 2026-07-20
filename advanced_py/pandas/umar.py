import pandas as pd 

df  = pd.DataFrame({
    "name": ["ali","umar","bob","salah"],
    "age" : [25,30,35,20],
    "city": ["lagos","nyc","la","ibadan"],
    "salary": [70000,80000,15000,90000]
})



u = df[["name", "age"]]


print(f" {'-'*16} ==end")
print(df.loc[0:2,["name","age"]])
print("end ============= +++++++++++++++++++")



print("FOR OUR I LOC =================")
print(df.iloc[0])
print("END OF Iloc ===================")

print(u)



print(df.shape)
print(df.head())



