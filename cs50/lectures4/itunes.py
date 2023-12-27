import json
import requests
import sys


if len(sys.argv) !=2:
    sys.exit()
response = requests.get("https://itunes.apple.com/search?entity=songs&limit=50&term="+sys.argv[1])
# print(response.json())
# print(json.dumps(response.json(), indent = 2))
o = response.json()
for result in o["queryParameters"]:
    print(result["country"])
