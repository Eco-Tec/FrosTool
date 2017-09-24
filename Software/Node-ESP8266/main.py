"""
    DESCRIPCI?N...
    This software is free, licensed y distributed under GPL v3.
    (see COPYING) WITHOUT ANY WARRANTY.
    You can see a description of license here: http://www.gnu.org/copyleft/gpl.html
    Copyright(c) 2017 by fandres "Fabian Salamanca" <fabian.salamanca@openmailbox.org>
    Distributed under GPLv3+
    Author - Fabian A. Salamanca F.
           -
    Hardware: ESP8266
    Pin distribution(Default)
    Pin 4   ->  Pin sensor(DHT11/DHT22), Data(IN)
    Pin 2   ->  Debug Visual(Default=Off), Led On Userled: for development board ESP8266
    Configure wifi and MQTT
"""
# --- Imports
# Hardware
import machine
import esp
import dht
# Files
# Micropython SW
from umqtt.simple import MQTTClient
import time

# --- Config
# Global
debug_mode = 1  # Debug On:1 | Off:0
# Pins
pin_sensor = 4
# --- HW, Obj
pin_led_debug = None  # pin_led_debug = machine.Pin(2, machine.Pin.OUT)  # Debug visual
client_mqtt = None  # Clienet MQTT
s_dht = None  # Sensor


def wifi_connect():
    "Conecta a la Red Wifi"
    import network
    from config import SSID, PASSWORD
    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)
        if not sta_if.isconnected():
            if debug_mode == 1:
                print('connecting to network...')
            sta_if.active(True)
            sta_if.connect(SSID, PASSWORD)
            while not sta_if.isconnected():
                if debug_mode == 1:
                    print('network config:', sta_if.ifconfig())
                else:
                    pass


def MQTTclient():
    "Protocolo MQTT en modo cliente, Configuración"
    from ubinascii import hexlify
    from machine import unique_id
    from config import BROKER
    global client_mqtt
    CLIENT_ID = hexlify(unique_id())
    client_mqtt = MQTTClient(CLIENT_ID, BROKER)


def debugMode():
    "Activa/Desactiva El debug (visual y de consola). On:1 | Off:0"
    if debug_mode == 1:
        global pin_led_debug
        esp.osdebug(1)  # turn on/off vendor O/S debugging messages
        pin_led_debug = machine.Pin(2, machine.Pin.OUT)  # Debug visual
    else:
        esp.osdebug(0)


def sensorConected():
    "Conmuta entre los diferentes sensores: DHT11/DHT22..."
    global s_dht
    s_dht = dht.DHT22(machine.Pin(pin_sensor))
    # s_dht = dht.DHT11(machine.Pin(pin_sensor))
    if debug_mode == 1:
        print('Sensor:', s_dht)


def readData():
    "Obtiene de lso sensores los datos de Temperatura/Humedad"
    s_dht.measure()  # Lectura de sensor DHT11/22
    if debug_mode == 1:
        print("Temperatura ", s_dht.temperature())  # Debug
        print("Humedad  ", s_dht.humidity())  # Debug
        pin_led_debug.value(not pin_led_debug.value())  # Debug visual


def MQTTSend():
    "Envio Datos mediante el protocolo MQTT"
    from config import TOPIC1, TOPIC2
    try:
        client_mqtt.connect()
        client_mqtt.publish(TOPIC1, str(s_dht.temperature()))
        client_mqtt.publish(TOPIC2, str(s_dht.humidity()))
        time.sleep_ms(200)
        client_mqtt.disconnect()
    except Exception as error:
        print("Error, MQTT", error)


def setup():
    " Inicializa y configura el dispositivo "
    debugMode()
    wifi_connect()
    MQTTclient()
    sensorConected()
    # loop
    readData()  # Lectura de sensores
    MQTTSend()  # Enviar datos mediante el protocolo MQTT


def loop():
    "Bucle principal infinito"
    pass
    # while True:  # beak: interrupt, Pin
    #     readData()  # Lectura de sensores
    #     MQTTSend()  # Enviar datos mediante el protocolo MQTT


# ######################     MAIN    #######################
if __name__ == '__main__':
    try:
        setup()
        loop()
    finally:
        pass
