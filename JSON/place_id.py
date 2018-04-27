import urllib.request, urllib.parse, urllib.error,urllib
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address_input = input('Enter location: ')
    if len(address_input) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'sensor':'false', 'address': address_input})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    place_id = js["results"][0]["place_id"]
    print(place_id)
