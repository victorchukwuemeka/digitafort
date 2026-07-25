
data = [3, 6, 9, 12, 15]
print(len(data))
range_len = len(data) - 1
print(range_len)


print("++++ the Range ===========  Data ")
for i in range(range_len):
    s_data = data[i + 1] - data[i]
    print(s_data)


s_data = [data[i + 1]- data[i] for i in range(len(data) -1)]
print(s_data)
