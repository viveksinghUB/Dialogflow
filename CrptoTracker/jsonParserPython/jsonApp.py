import urllib
import json

url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR'
result = json.load(urllib.urlopen(url))

print result['BTC']
