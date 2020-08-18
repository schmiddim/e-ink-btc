import requests as r
import dateutil.parser
from millify import millify

def get_ticker(symbol):
    """
    What to display?
    - Last Price   'last_price'
    - 24h high 'high'
    - 24h low  'low'
    - 24h volume 'quote_volume'
    Bonus
    - Gewinn
    - 24h Price Change %  'price_change_percentage'
    https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT_(B)
    """

    url = 'https://api.exchange.bitpanda.com/public/v1/market-ticker'
    result = r.get(url).json()

    for item in result:
        if item.get('instrument_code') == symbol:
            item['time'] = dateutil.parser.parse(item.get('time'))
            item['quote_volume'] = int(float(item.get('quote_volume')))
            return item


r = get_ticker('BTC_EUR')
print(millify(r.get('quote_volume'), precision=3), )

foo = 4

print(r)
