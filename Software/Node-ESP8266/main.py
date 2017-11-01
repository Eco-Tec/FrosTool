"""
    DESCRIPCI?N...
    This software is free, licensed y distributed under GPL v3.
    (see COPYING) WITHOUT ANY WARRANTY.
    You can see a description of license here: http://www.gnu.org/copyleft/gpl.html
    Copyright(c) 2017 by fandres "Fabian Salamanca" <fabian.salamanca@openmailbox.org>
    Distributed under GPLv3+
    Based On https://github.com/fandres/Monitor-heladas/blob/master/Code/main.py
    Author  - Fabian A. Salamanca F (@fandres).
            - Marlon mauricio Moreno (@mau_rinc2010).
    Hardware: ESP8266
    Pin distribution(Default)
    Pin 4   ->  Pin sensor(DHT11/DHT22), Data(IN)
    Pin 2   ->  Debug Visual(Default=Off), Led On Userled: for development board ESP8266
"""


from MQTT import MQTT
from wifi import WIFI
from cultivo import Cultivo
from debug import debug_mode
import machine


if __name__ == '__main__':
    # configurando RTC.ALARM0
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
    # Si el dispositivo desperto de el modo deep sleep
    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
        # print('Desperto del modo deep sleep')  # Debug
        try:
            debug = debug_mode(False)  # True Or False
            wifi = WIFI(debug)
            mqtt = MQTT(debug)
            wifi.connect()
            cultivo = Cultivo(debug, mqtt)
            cultivo.read_sensores()
            cultivo.send_data()
        except:
            import machine
            machine.reset()
    rtc.alarm(rtc.ALARM0, 10000)
    machine.deepsleep()
