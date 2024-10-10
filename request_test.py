import requests

url = "https://jsonplaceholder.typicode.com/posts/5"

response = requests.get(url)
print (response)
