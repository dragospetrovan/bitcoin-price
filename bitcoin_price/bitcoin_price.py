from flask import Flask
from flask import render_template
import urllib.request as urllib2
import json


req = urllib2.Request('https://apiv2.bitcoinaverage.com/indices/global/history/BTCUSD?period=minute')
req.add_header( 'x-ba-key', 'ZDg2NWRkMTdiN2RiNDU2NjkyYjA0YWZjZTRiMWNiNzA')
resp = urllib2.urlopen(req)
data_json = json.loads(resp.read())
import itertools
bitcoin_values = []
for i in range(0, 10):
    array=(data_json[i])
    bitcoin_values.append(array['average'])
    bitcoin_10min_average_price=sum(bitcoin_values)/len(bitcoin_values)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', passed_bitcoin_10min_average_price=bitcoin_10min_average_price)


if __name__ == '__main__':
    app.run('0.0.0.0', '80')