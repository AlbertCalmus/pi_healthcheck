import requests

url = 'http://192.168.1.10:7778/receive-ip'

myobj = {'names': 'theo','ip':'123.151'}
x = requests.post(url, json = myobj)

print(x.text)