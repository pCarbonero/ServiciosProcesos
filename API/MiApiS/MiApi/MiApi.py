from telnetlib import DO
from pip._vendor import requests

num = 1
while num != 0:
    num = int(input("Inserta numero "))
    api_url = "https://jsonplaceholder.typicode.com/todos/" + str(num)
    reponse = requests.get(api_url)
    print(reponse.json())

print("adios")




