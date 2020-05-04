import json
import requests
urltoget = "https://api.worldtradingdata.com/api/v1/history"
addons = "?api_token=7CMPTfmuoftI3jkNJe3ryjoH4Kz3avhsijs8iexm18ZXMqQFl4ENRhDIpxNx&symbol=TWTR"
urltoget+=addons
#ampersand sign (&)

response = requests.get(urltoget)

response.status_code
dictionaries = response.json()
print(response.text)#The response in a string format, but still, since it is a string, it can't be used as a normal dictionary

response.content#in bytes format
print("\n\n\n",json.dumps(response.json(),indent=4))