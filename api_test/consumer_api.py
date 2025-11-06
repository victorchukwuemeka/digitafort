import requests

res  = requests.get('https://jsonplaceholder.typicode.com/users')

if res.status_code ==  200:
    data = res.json()
    print(data)
else:
    print(f"Error: {res.status_code}")

new_user = {
    'name' : 'mo solah',
    'email': 'good@gmail.com',
    'age': 39
}

res = requests.post('https://jsonplaceholder.typicode.com/users', json=new_user)

if res.status_code == 201:
    create_user  = res.json()
    print(f"user created with ID:{create_user['id']}")


update_user = {
    'name' : 'john snow',
    'email': 'snow@gmail.com',
    'age': 40
}
res = requests.put('https://jsonplaceholder.typicode.com/users/5', json=update_user)
if res.status_code == 200:
    print("cool  done ")

res = requests.patch('https://jsonplaceholder.typicode.com/users/5', json={'age':50})
age = res.json()
print(f"new age: {age['age']}")


res = requests.delete('https://jsonplaceholder.typicode.com/users/5')
#print(res)
if res.status_code == 204:
    print("GONE for GOOD")




headers = {'Authorization': 'Token your-token-here'}
response = requests.get('https://api.example.com/profile', headers=headers)