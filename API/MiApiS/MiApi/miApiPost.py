from pip._vendor import requests

api_url = "https://jsonplaceholder.typicode.com/todos"

id = int(input("Inserta el id del usuario "))
tit = input("El titulito: ")
completed = True if(input("Completo? ") == "si") else False

todo = {"userId": id, "title": tit, "completed": completed}
reponse = requests.post(api_url, json=todo)  

#imp
print(reponse.json())

print("Code estado: ", reponse.status_code)

#id = int(input("Inserta el id del usuario "))
#tit = input("El titulito: ")
#completed = True if(input("Completo?") == "si") else False