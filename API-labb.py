import requests

response = requests.get('https://api.cat-fact.herokuapp.json')
print(response.json())