import requests

post_id = 1
url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'
response = requests.get(url)



if response.status_code >= 400:
    print(f"Error: {response.status_code}")
else:
    print(response.json())

class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed


new_object = ToDo(userId=1, id=201, title='10 push-ups at 9 am', completed=False)
new_todo_dict = {
    "userId": new_object.userId,
    "id": new_object.id,
    "title": new_object.title,
    "completed": new_object.completed
}

url_post = 'https://jsonplaceholder.typicode.com/todos'
response_post = requests.post(url_post, json=new_todo_dict)

if response_post.status_code >= 400:
    print(f"Error: {response_post.status_code}")
else:
    print(response_post.json())

new_object.title = '20 pull ups at 20pm'
new_todo_dict["title"] = new_object.title

chosen_id = 201
url_put = f'https://jsonplaceholder.typicode.com/todos/{chosen_id}'
response_put = requests.put(url_put, json=new_todo_dict)

if response_put.status_code >= 400:
    print(f"Error: {response_put.status_code}")
else:
    print(response_put.json())

