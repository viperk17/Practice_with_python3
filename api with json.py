import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/currency-converter/") as response:
    source = response.read()

print(source)
data = json.loads(source)
print(data)

# print(len(data['list']['resources']))
# print(json.dumps(data, indent=2))

# usd_rates = dict()
#
# for item in data['list']['resources']:
#     name = item['resource']['fields']['name']
#     price = item['resource']['fields']['price']
#     usd_rates[name] = price
#
# print(50 * float(usd_rates['USD/INR']))
