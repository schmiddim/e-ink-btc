import sys
import os
import requests as r

libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')

if not os.path.exists(picdir):
    raise Exception("picdir {} not found".format(picdir))

if os.path.exists(libdir):
    sys.path.append(libdir)
else:
    raise Exception("libdir {} not found".format(libdir))
import logging
from waveshare_epd import epd2in7

from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.DEBUG)


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
            return item


try:
    result = get_ticker('BTC_EUR')
    logging.info(result)

    print(os.path.join(picdir, 'Font.ttc'))
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)

    epd = epd2in7.EPD()
    epd.init()
    epd.Clear(0xFF)

    base = 40
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'Last ' + result.get('last_price') + '€', font=font35, fill=0)
    draw.text((10, base), 'H ' + result.get('high') + '€ / ' + 'L ' + result.get('low') + '€', font=font18, fill=0)
    draw.text((10, base + 22), '24h:' + result.get('price_change_percentage') + '%', font=font35, fill=0)
    draw.text((10, base + 22 + 22 + 22), 'Volume ' + result.get('quote_volume') + ' €', font=font18, fill=0)
    draw.text((10, 150), result.get('time'), font=font18, fill=0)
    epd.display(epd.getbuffer(Himage))


except IOError as e:
    logging.error(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in7.epdconfig.module_exit()
    exit()
