import requests

request = requests.get('https://www.wikipedia.org')
print(request.text)

file = open("url Data.txt","w")

file.write(request.text)

file.close()