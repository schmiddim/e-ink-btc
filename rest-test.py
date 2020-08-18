


import requests as r

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

    url= 'https://api.exchange.bitpanda.com/public/v1/market-ticker'
    result =r.get(url).json()

    for item in result:
        if item.get('instrument_code') == symbol:
            return item

r= get_ticker('BTC_EUR')
foo =4

print(r)