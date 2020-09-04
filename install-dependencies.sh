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
sudo apt-get update; apt-get upgrade
sudo apt-get install -y python3-pip  python3-pil  python3-numpy screen;
sudo apt-get install -y libopenjp2-7 libtiff5

echo Install pip dependencies
pip3 install -r requirements.txt



###nightmare wifi driver @see https://www.raspberrypi.org/forums/viewtopic.php?p=462982#p462982
cd /tmp
sudo wget http://downloads.fars-robotics.net/wifi-drivers/install-wifi -O /usr/bin/install-wifi
sudo chmod +x /usr/bin/install-wifi
sudo install-wifi -c rpi-update
sudo rpi-update


#maybe ifconfig wlan1 up