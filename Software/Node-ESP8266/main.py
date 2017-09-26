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

#from config import TOPIC1, TOPIC2
from cultivo import cultivo
from MQTT import MQTT
from wifi import WIFI
from debug import debug_mode


if __name__ == '__main__':
<<<<<<< HEAD
    debug=debug_mode(True)
    #mqtt = MQTT(debug)
    #wifi = WIFI(debug)
    #wifi.connect()
    cultivo=cultivo(debug)
    cultivo.read_sensores()
    #sensor1 = DHT22(debug,"DHT22",4)

    #print(sensor1.readData())
=======
    debug = debug_mode(True)
    mqtt = MQTT(debug)
    wifi = WIFI(debug)
    sensor1 = DHT22(debug, "DHT22", 4)
    # wifi.connect()
    print(sensor1.readData())
>>>>>>> c808205e1b9b8887ca523e2693a3a74856aa4cb5
    #mqtt.send(TOPIC1, temperatura)
    #mqtt.send(TOPIC2, humedad)
