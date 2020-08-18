#!/bin/bash

#@see https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT_(B)

echo Install BCM2835 libraries

cd /tmp/
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
tar zxvf bcm2835-1.60.tar.gz
cd bcm2835-1.60/
sudo ./configure
sudo make
sudo make check
sudo make install

echo Install Python system packages
sudo apt-get install -y python3-pip  python3-pil  python3-numpy screen;

echo Install pip dependencies
pip3 install RPi.GPIO spidev python-dateutil millify