import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

key1 = 5
key2 = 6
key3 = 13
key4 = 19

tic = 0

GPIO.setup(key1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(key4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
from modules.views import draw_chart


def write_symbol_to_file(symbol):
    with open('./symbol-to-show.txt', 'w+') as out:
        out.write(symbol)


def interrupt(channel):
    symbol = 'BTC_EUR'
    if channel == key1:
        symbol = 'BTC_EUR'
    if channel == key2:
        symbol = 'ETH_EUR'
    if channel == key3:
        symbol = 'XRP_EUR'
    if channel == key4:
        symbol = 'MIOTA_EUR'
    print(channel, 'draw ', symbol)
    write_symbol_to_file(symbol)
    draw_chart(symbol)


GPIO.add_event_detect(key1, GPIO.FALLING, callback=interrupt, bouncetime=200)
GPIO.add_event_detect(key2, GPIO.FALLING, callback=interrupt, bouncetime=200)
GPIO.add_event_detect(key3, GPIO.FALLING, callback=interrupt, bouncetime=200)
GPIO.add_event_detect(key4, GPIO.FALLING, callback=interrupt, bouncetime=200)

try:
    while True:
        tic = tic + 1
        print("Tic %d" % tic)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nBye")
