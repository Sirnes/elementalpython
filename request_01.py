import requests

rec = requests.get('http://localhost/jornal/public/index')

print(rec.headers)