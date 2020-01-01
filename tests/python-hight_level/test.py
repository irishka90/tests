import requests
import json

client_id = '337b66c005135660a4b5'
client_secret = '08cf36bcb60ee68df575c1c1e2ac65f5'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  }, timeout=5)
j = r.json()
headers = {"X-Xapp-Token": j["token"]}
url_base = "https://api.artsy.net/api/artists/{}"

d = {}

with open("in.txt", 'r') as reader:
    for line in reader:
        url = url_base.format(line.strip())
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            key = int(data["birthday"])
            if key not in d.keys():
                d[key] = []
            d[key].append(data["sortable_name"])

keys = sorted(d.keys())

with open("out.txt", 'w') as file:
    for it in keys:
        names = sorted(d[it])
        for name in names:
            file.write(name)
            file.write("\n")
