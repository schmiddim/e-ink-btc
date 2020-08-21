from modules.views import draw_chart
import os

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'symbol-to-show.txt')

try:
    with open(path) as out:
        symbol = out.read()
except EnvironmentError:
    symbol = 'BTC_EUR'
draw_chart(symbol)
