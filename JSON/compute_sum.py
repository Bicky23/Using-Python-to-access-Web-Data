import urllib.request, urllib.parse, urllib.error
import json

f = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_61148.json')
data = f.read().decode()
print('----------------------------------')

info = json.loads(data)
comments = info["comments"]
net = 0
for dic in comments:
    if 'count' in dic.keys():
        net += dic['count']
    else:
        pass
print(net)
