import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://py4e-data.dr-chuck.net/comments_61147.xml'
uh = urllib.request.urlopen(serviceurl)
data = uh.read()
print('Retrieved')
print('--------------')
# print(data.decode())
tree = ET.fromstring(data)

results = tree.findall('.//count')
net = 0
for tag in results:
    net += int(tag.text)

print(net)
