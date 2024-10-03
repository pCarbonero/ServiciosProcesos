from pip._vendor import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"

reponse = requests.get(api_url)
print(reponse.json())

todo = { "title": "Wakala"}

reponse = requests.patch(api_url, json = todo)

print(reponse.json())
print(reponse.status_code)
