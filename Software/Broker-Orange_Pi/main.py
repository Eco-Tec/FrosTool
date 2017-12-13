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
#import OPi.GPIO as GPIO
# imports modulos
#from config import BROKER
import paho.mqtt.client as mqtt
# imports library python
from time import sleep
import threading
from time import time, sleep
import re
import queue


##########----------    Class   ----------##########
class SaveData (object):
    """ Clase que almacena los datos de los diferentes sensores
    para cada sensor, esta clase se debe instanciar."""

    def __init__(self, ruta):
        """Se define el nombre del archivo para cada sensor"""
        #self.name_topic = str(sensor)
        #self.data = data
        #self.time = time
        self.ruta = str(ruta)
        #self.archivo = ""
        # self.crear_archivo()
        self.archivos = {}

    def set_ruta(self, ruta):
        """Metodo para cambiar la ruta en la cual se guarda el archivo"""
        self.ruta = str(ruta)
        # self.crear_archivos()

    def add_file(self, name):
        """Crea un archivo nuevo y lo agrega al diccionario """
        self.archivos[name] = self.ruta + str(name) + ".txt"

    def add_dato(self, dato):
        """"Guarda un nuevo dato, si el archivo no existe lo creea"""
        print(dato)
        if dato[1] in self.archivos:
            a = open(self.archivos[dato[1]], 'a')
            a.write(dato[3] + "\n")
            a.close()
        else:
            # crea un nuevo archivo y guarda el dato
            self.add_file(dato[1])
            a = open(self.archivos[dato[1]], 'w')
            a.write(dato[3] + "\n")
            a.close()


##########----------    Class   ----------##########
class Prediction(object):
    """Algoritmo que permite hasta cierto grado la prediccion"""

    def __init__(self, arg):
        super(Prediction, self).__init__()
        self.arg = arg


##########----------    Class   ----------##########
class ClassName(object):
    """docstring for ."""

    def __init__(self, arg):
        super(self).__init__()
        self.arg = arg
        # Control(object):
    """Manipula los actuadores, como la alarma visual sonora,
    ademas de otros actuadores como los sistemas de riego..."""

    def __init__(self, PIN_Alarm=17, PIN_Sp_A=4):
        super(Actuators, self).__init__()
        self.PIN_ALARMA = PIN_Alarm
        self.PIN_STOP_ALARMA = PIN_Sp_A
        self._alarm_state = 0
        self._SET_TEMP = 0
        self._SET_HUM = 80
        GPIO.output(PIN_ALARMA, False)
        GPIO.setup(PIN_STOP_ALARMA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        # add rising edge detection on a channel
        GPIO.add_event_detect(PIN_STOP_ALARMA, GPIO.RISING,
                              callback=self.alarmaCallback)

    def alarmaCallback(PIN_STOP_ALARMA):
        "Metodo que desactiva la alarma. INTERRUPT"
        if self._alarm_state == 1:
            pass  # Publique


##########----------    Class   ----------##########
class BrokerManager(threading.Thread):
    """Clase que gestiona el Broker, la activacion y pausa de la alarma
    Ademas de lavisualizacion de los datos obtenidos y sus estados"""

    def __init__(self, ip="localhost", port=1883):
        threading.Thread.__init__(self)
        self.data = SaveData("/home/game/")
        self.Client = mqtt.Client()
        self._ip = ip
        self._port = port
        self.Client.on_connect = self.on_connect
        self.Client.on_message = self.on_message

    def set_ip(self, ip):
        "instancia la Ip usada por el Broker"
        self.ip = ip

    def set_port(self, port):
        "intancia el puerto MQTT"
        self.port = port

    def on_connect(self, client, userdata, flags, rc):
        # print("Connected with result code "+str(rc))  # Debug
        client.subscribe("/#")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        dic = {}
        lists = []
        m = ""
        d = False
        for a in msg.topic:
            if a != '/':
                m = m + a
            elif a == '/':
                if m != "":
                    lists.append(m)
                m = ""
        lists.append(m)
        lists.append(str(msg.payload))
        ##data = {sensor: {msg.topic, str(msg.payload)[2:-1]}}
        self.data.add_dato((lists))
        # self.data.add_dato(msg)
        print(lists)

    def connect(self):
        self.Client.connect(self._ip, self._port, 60)

    def disconnect(self):
        self.Client.disconnect()

    def run(self):
        self.Client.loop_forever()


class main():
    def __init__(self):
        self.BrokerManager = BrokerManager(ip="localhost", port=1883)
        self.BrokerManager.connect()
        self.BrokerManager.start()  # inicia el hilo
        self.hilo_padre = {}
        self.hilo_hijo = {}
        print("Broker 4")
        a = 0
        while a < 50:
            sleep(1)
            a = a + 1
            print("halo")
        self.BrokerManager.disconnect()

    def add_hilos(self, hilo_padre, hilo_hijo):
        cola = Queue.Queue()
        self.hilo_padre[hilo_padre] = Recepcion(cola)
        cola = Queue.Queue()
        self.hilo_hijo[hilo_hijo] = cola

    # def hilos(self):
    #    pass


##########----------    Main   ----------##########
if __name__ == '__main__':
    main = main()
