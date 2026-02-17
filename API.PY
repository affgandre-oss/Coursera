import urllib.request
import urllib.parse
import json
serviceurl = "http://py4e-data.dr-chuck.net/opengeo"
address = input("Enter location: ")
params = {'q': address}
url = serviceurl + '?' + urllib.parse.urlencode(params)
print('Retreving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrevied", len(data), "characters")
js = json.loads(data)
plus_code = js['features'][0]['properties']["plus_code"]
print("Plus code", plus_code)