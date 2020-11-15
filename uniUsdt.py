import urllib.request , json
import sys
from sendMail import sendMail

URL = "https://www.binance.com/api/v3/depth?symbol=UNIUSDT&limit=5"
price = 0



with urllib.request.urlopen(URL) as url:
    data = json.loads(url.read().decode())
    price = float(data['bids'][0][0])

if (price == 0 or price < 5):
    sys.exit()    



sendMail("""
    Subject: UNIUSDT Alarm
    Hello Ali
    UNIUSDT price now is good for sell.
    price : {} 
""".format(price))




