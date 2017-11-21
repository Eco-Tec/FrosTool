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
    Pin X [BOARD]    ->  Pin: Alarm(Buzer): [OUT]
    Pin X [BOARD]    ->  Pin: Stop Alarm(Buzer): [IN]
    Configure wifi and MQTT
"""
__author__ = "Fabian A. Salamanca F."
__copyright__ = "Copyright 2017, Eco-Tec"
__credits__ = ["Fabian A. Salamanca F."]
__license__ = "GPL"
__version__ = "3.0"
__maintainer__ = __author__
__email__ = "fabian.salamanca@gmail.com"

# imports hardware
import OPi.GPIO as GPIO
# imports modulos
from config import BROKER
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish
# imports library python
from time import sleep


if __name__ == '__main__':

    try:
        pass
    except:
        pass
