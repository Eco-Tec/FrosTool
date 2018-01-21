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

# imports hardware
# imports modulos
from bootloader import Bootloader
# imports library python
# imports library Micro-python
import machine

if __name__ == '__main__':
    # configurando RTC.ALARM0
    boot = Bootloader()
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
        # boot.read_config()
        boot.run_boot()

    rtc.alarm(rtc.ALARM0, 5000)
    machine.deepsleep()
