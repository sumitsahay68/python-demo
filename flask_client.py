import requests

url = "http://localhost:5000/"

result = requests.get(url).json()
print (result)
result = requests.post(url).json()
print (result)


url= "http://localhost:5000/abc/"

result= requests.get(url).json()
print (result)
result = requests.post(url).json()
print (result)


url = "http://localhost:5000/cube/"
num = input("Enter Number: ")
url = url+num
result = requests.get(url).json()
print(result)
