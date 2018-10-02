import json
import requests
import API
x = int(1)
while x < 600:
    r = requests.get('https://cex.io/api/order_book/ETH/EUR/')
    json_data = json.loads(r.text)
    tradefee = 0.0016
    topask = json_data['asks'][000][0]
    topbid = json_data['bids'][000][0]
    netProfit = (topask * (1 - tradefee)) - (topbid * (1 + tradefee))
    if netProfit > 0:
        print('Profit')
    else:
        print('Loss')
    netFee = (topask + topbid) * tradefee
    print(netFee)
    x += 1

requests.get('https://cex.io/api/balance/')

APIrequest = API()
