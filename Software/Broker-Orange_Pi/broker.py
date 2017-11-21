#!/usr/bin/env python
"""
    DESCRIPCI?N...
    This software is free, licensed y distributed under GPL v3.
    (see COPYING) WITHOUT ANY WARRANTY.
    You can see a description of license here: http://www.gnu.org/copyleft/gpl.html
    Copyright(c) 2017 by fandres "Fabian Salamanca" <fabian.salamanca@openmailbox.org>
    Distributed under GPLv3+
    Hardware: Orange Pi Zero
    Pin distribution(Default)
    Pin X     ->  Pin: Alarm(Buzer): [OUT]
    Pin X     ->  Pin: Stop Alarm(Buzer): [IN]
    Configure wifi and MQTT
    library:
    https://github.com/eclipse/paho.mqtt.python
"""
__author__ = "Fabian A. Salamanca F."
__copyright__ = "Copyright 2017, Eco-Tec"
__credits__ = ["Fabian A. Salamanca F."]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = __author__
__email__ = "fabian.salamanca@gmail.com"


import os
import sys
from pyA20.gpio import gpio
#from pyA20.gpio import connector
from pyA20.gpio import port
from time import sleep

led = port.PA12

gpio.init()
gpio.setcfg(led, gpio.OUTPUT)

try:
    print ("Press CTRL+C to exit")
    while True:
        gpio.output(led, 1)
	print "led set 1 \r\n"
        sleep(5)
        gpio.output(led, 0)
	print "led set 0 \r\n"
        sleep(5)
except KeyboardInterrupt:
	print ("Goodbye.")
