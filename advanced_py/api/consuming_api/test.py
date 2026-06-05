import requests

res = requests.get("https://jsonplaceholder.typicode.com/users")
print(res.status_code)
print(res.json())
print(res.text)
print(res.headers)


#params = {"page": 2, "limit": 10}
#response = requests.get("https://jsonplaceholder.typicode.com/users", params=params)
#print(response)