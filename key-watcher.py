import RPi.GPIO as GPIO
import time
import json
import os
import shutil
from modules.views import draw_chart

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

path_settings = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.json')
dist_path_settings = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.json.dist')
settings ={}
if not os.path.isfile(path_settings):
    dist_path_settings = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'settings.json.dist')
    shutil.copyfile(dist_path_settings, path_settings)
with open(path_settings) as out:
    settings = json.load(out)


def write_symbol_to_file(symbol):
    with open('./symbol-to-show.txt', 'w+') as out:
        out.write(symbol)


def interrupt(channel):
    symbol = 'BTC_EUR'
    if channel == key1:
        symbol = settings.get('keyMappings').get('key1')
    if channel == key2:
        symbol = settings.get('keyMappings').get('key2')
    if channel == key3:
        symbol = settings.get('keyMappings').get('key3')
    if channel == key4:
        symbol = settings.get('keyMappings').get('key4')
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
