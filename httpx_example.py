from pprint import pprint

import httpx

BASE_URL_1 = 'https://httpbin.org/post'

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.json())

data = {
    "userId": 1,
    "title": "new task",
    "completed": True
}

response = httpx.post(url='https://jsonplaceholder.typicode.com/todos', json=data)

print(response.json(), response.status_code)

files = {"file": ('my_file.txt', open('my_file.txt', 'rb'))}

response = httpx.post(BASE_URL_1, files=files)

print(response.is_success)
print(response.status_code)
pprint(response.json())
