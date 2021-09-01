import requests
  
address = "0xd1EF5ea82FbEFc3ae249a053d8Ed9C5d74c6a630"
URL = f"http://api.ethplorer.io/getAddressInfo/{address}"
  
apiKey = "EK-jfm12-oYthmCw-sGE1Q"
  
PARAMS = {'apiKey': apiKey}
r = requests.get(url = URL, params = PARAMS)
  
data = r.json()
for i in data["tokens"]:
    tokenInfo = i["tokenInfo"]
    print("{} Price: {}".format(tokenInfo["name"], tokenInfo["price"]["rate"]))

print("ETH balance " + str(data["ETH"]["balance"])