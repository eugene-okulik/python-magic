import requests
from datetime import datetime


start = datetime.now()
response = requests.get('http://okulik.site:52355/meme/276', headers={'Authorization': '6hN7IJqlCkGYfHJ'})
print(response)
end = datetime.now()
print(end - start)
