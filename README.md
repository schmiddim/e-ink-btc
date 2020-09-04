# Bitcoin Price on E-Paper
![Example Image](/pic/20200818_174441.jpg)

## About 
Display BTC Price Information from Bitpanda on a RaspberryPI


## Hardware
1. [Raspberry PI (Version 3 is enough)](https://amzn.to/3aCpsph)
2. [e-Paper Display](https://amzn.to/3aA24IZ)

## Sources
- https://github.com/waveshare/e-Paper
- https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT_(B)

## Installation
1. You need a Raspberry PI with an actual Version of Raspbian
2. Follow the Instructions in the [Waveshare Wiki](https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT_(B)) or run **install-dependencies.sh**
3. Clone the Repo in your homedir
4. [Configure SPI](https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/)
5. Execute the display.py script

## Usage
Crontab
```
*/5 * * * * python3 /home/pi/e-ink-btc/display.py
```

Button Support (very slow at the moment)
```
screen -S e-ink-btc-buttons python3 key-watcher.py

```


