#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    DESCRIPCI?N...
    This software is free, licensed y distributed under GPL v3.
    (see COPYING) WITHOUT ANY WARRANTY.
    You can see a description of license here: http://www.gnu.org/copyleft/gpl.html
    Copyright(c) 2017 by fandres "Fabian Salamanca" <fabian.salamanca@openmailbox.org>
                         Marlon...
    Distributed under GPLv3+
    Hardware: Orange Pi Zero
    Pin distribution(Default)
    Pin X [BOARD]    ->  Pin: Alarm(Buzer): [OUT]
    Pin X [BOARD]    ->  Pin: Stop Alarm(Buzer): [IN]
    Configure wifi and MQTT
"""


__author__ = "Fabian A. Salamanca F."
__copyright__ = "Copyright 2017, Eco-Tec"
__credits__ = ["Fabian A. Salamanca F, Marlon..."]
__license__ = "GPL V3.0"
__version__ = "1.4"
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
import time
import re
import queue
from config import*

##########----------    Class   ----------##########


class Archivos ():
    def __init__(self):
        self.plantilla = ""  # open("plantilla.txt",'r')
        self.file = ""

    def crear_file(self, name_file, broker, ubicacion, nodo, sensor, var):
        self.plantilla = open("plantilla.txt", 'r')
        self.file = open(name_file, 'w')
        self.encabezado(broker, ubicacion, sensor, nodo, var)
        self.file.close()
        self.plantilla.close()

    def encabezado(self, broker, ubicacion, sensor, nodo, var):
        linea = self.plantilla.readline()
        while linea != "":

            if linea == "# Copyrigh\n":
                #m=re.sub("\s", __copyright__ ,linea)
                self.file.write("# " + __copyright__ + "\n")
            elif linea == "# License\n":
                # print("# "+__copyright__+"\n")
                m = re.sub("\n", "  ," + __license__ + "\n", linea)
                # print(m)
                self.file.write(m)
            elif linea == "# Version\n":
                # print("# "+__copyright__+"\n")
                m = re.sub("\n", "  ," + __version__ + "\n", linea)
                # print(m)
                self.file.write(m)
            elif linea == "# Generado por el Broker\n":
                m = re.sub("\n", "  ," + broker + "\n", linea)
                # print(m)
                self.file.write(m)
            elif linea == "# fecha\n":
                m = re.sub("\n", "  ," + time.strftime("%d/%m/%y") + "\n", linea)
                # print(m)
                self.file.write(m)
            elif linea == "# UBICACION\n":
                m = re.sub("\n", "  " + ubicacion + "\n", linea)
                # print(m)
                self.file.write(m)
            elif linea == "# SENSOR\n":
                m = re.sub("\n", "  ," + sensor + "\n", linea)
                # print(m)
                self.file.write(m)
            elif linea == "# NODO\n":
                m = re.sub("\n", "  ," + nodo + "\n", linea)
                # print(m)
                self.file.write(m)
            elif linea == "TIME,var\n":
                m = re.sub("var", var + "\n", linea)
                self.file.write(m)
            else:
                # print(linea)
                self.file.write(linea)
            linea = self.plantilla.readline()

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

    def __init__(self, main, ip="localhost", port=1883):
        threading.Thread.__init__(self)
        self.Client = mqtt.Client()
        self._ip = ip
        self._port = port
        self.Client.on_connect = self.on_connect
        self.Client.on_message = self.on_message
        self.archivos = main.archivos

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
        dato = re.sub("b", "", str(msg.payload))
        dato = re.sub("'", "", str(dato))
        try:
            name = self.archivos[msg.topic]
            print(name)
            self.add_dato(name, dato)
        except:
            print("Topico no valido")

    def add_dato(self, archivo, dato):
        """"Guarda un nuevo dato, si el archivo no existe lo creea"""
        # print(dato)
        a = open(archivo, 'a')
        a.write(time.strftime("%H:%M:%S") + "," + (dato) + "\n")
        a.close()

    def connect(self):
        self.Client.connect(self._ip, self._port, 60)

    def disconnect(self):
        self.Client.disconnect()

    def run(self):
        self.Client.loop_forever()


class main():
    def __init__(self):
        self.ruta = "/home/data/"
        self.csv = Archivos()
        self.archivos = {}

        self.BrokerManager = BrokerManager(self, ip="localhost", port=1883)
        self.BrokerManager.connect()
        self.BrokerManager.start()  # inicia el hilo

        self.hilo_padre = {}
        self.hilo_hijo = {}
        self.list_topic = {}
        self.generate_topic()
        # print(self.archivos)
        # print(self.list_topic)
        # for i in self.archivos:
        #    print("key "+  str(i)+ "  "+"value " + str(self.archivos[i]))
        print("Modo infinito")
        a = 0
        while True:  # a < 500:
            sleep(1)
            a = a + 1
            print("halo")
        self.BrokerManager.disconnect()

    def generate_topic(self):
        c = 0
        f = "/" + CULTIVO["TIPO_CULTIVO"]
        for i in LIST_SENSOR:
            # print("a"+i)
            for m in LIST_SENSOR[i]:
               # print(m)
                if "SENSOR" in m:
                    for n in LIST_SENSOR[i][m]:
                        topic = f + str(LIST_SENSOR[i][m][n][0]) + "/" + i + "/" + m
                        self.list_topic["topic_" + str(c)] = topic
                        name = str(LIST_SENSOR[i][m][n][1]) + "/" + i + "/" + m
                        name = re.sub("/", "_", name)
                        self.add_file(
                            name, topic, LIST_SENSOR[i][m][n][1], "," + LIST_SENSOR[i]["LOCATION"], i, m)
                        c = c + 1

    def add_file(self, name, topic, var, location, nodo, sensor):
        """Crea un archivo nuevo y lo agrega al diccionario """
        name = self.ruta + str(name) + "_" + time.strftime("%d_%m_%y") + "_" + ".csv"
        self.archivos[topic] = name
        # print(topic)
        self.csv.crear_file(name, BROKER["NUMBER_BROKER"], location, nodo, sensor, var)

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

