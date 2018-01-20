# imports hardware
# imports modulos
from config import NAME, key
from cultivo import Cultivo
from MQTT import MQTT
from wifi import WIFI
from debug import debug_mode
# imports library python
from time import sleep
# imports library Micro-python
#import machine
#import socket
<<<<<<< HEAD
import time
import socket

from umqtt.simple import MQTTClient
=======
>>>>>>> ba2436bf93881f03bb85bbd5c36ea9e33a0eeeaf


class Bootloader():
    def __init__(self):
        self.debug = ""
        self.wifi = ""
        self.mqtt = ""
        self.read = {}
        self.mode = False
        self.firmware = 1.0
<<<<<<< HEAD

        self.read_config()

    def run_boot(self):
        """Se entra en modo bootloader deacuerto a la solicitud del broker"""
        #self.read_config()
=======
        # self.config_boot = open("config_boot.txt", 'r+')
        # self.read_config()

    def run_boot(self):
        """Modo bootloader dada la solicitud del broker"""
        self.read_config()
>>>>>>> ba2436bf93881f03bb85bbd5c36ea9e33a0eeeaf
        if self.mode:
            print("modo boot")  # Debug
            self.debug = debug_mode(True)  # True Or False
            self.wifi = WIFI(self.debug)
            self.wifi.connect()
<<<<<<< HEAD
            self.mqtt = MQTT(self.debug)
            self.mqtt.connect()
            self.mqtt.send_boot("/firmware/" + NAME, self.firmware)
            self.save_file("plantilla.txt")
            self.mqtt.disconnect()
=======
            try:
                if self.wifi.sta_if.isconnected():
                    self.mqtt = MQTT(self.debug)
                    self.mqtt.connect()
                    self.mqtt.send_boot("/firmware/" + NAME, self.firmware)
                    self.mqtt.disconnect()
            except OSError:
                import machine
                machine.reset()
>>>>>>> ba2436bf93881f03bb85bbd5c36ea9e33a0eeeaf
        else:
            print("modo user")
            self.run_user()

    def set_firmware(self, version):
        """DOCSTRSINGS"""
        self.firmware = version

    def set_mode(self, mode):
        """DOCSTRSINGS"""
        self.mode = mode

    def salvar_modo(self):
<<<<<<< HEAD
        a = open("config_boot.txt", 'r+')
        c = a.tell()
        ar = a.readline()
        while ar != "":
            am = ar.split(" = ")
            if am[0] == "MODE":
                a.seek(c)
                a.write("MODE = " + str(self.mode) + '\n')
            elif am[0] == "FIRMWARE":
                a.seek(c)
                a.write("FIRMWARE = " + str(self.firmware) + '\n')
            c = a.tell()
            ar = a.readline()
        a.close()
=======
        """DOCSTRSINGS"""
        file_config_boot = open("config_boot.txt", 'r+')
        file_read_line = file_config_boot.readline()
        while file_read_line != "":
            file_line_split = file_read_line.split(" = ")
            if file_line_split[0] == "MODE":
                file_config_boot.write("MODE = " + str(self.mode) + '\n')
            elif file_line_split[0] == "FIRMWARE":
                file_config_boot.write(
                    "FIRMWARE = " + str(self.firmware) + '\n')
            file_read_line = file_config_boot.readline()
        file_config_boot.close()
>>>>>>> ba2436bf93881f03bb85bbd5c36ea9e33a0eeeaf
        self.print_txt()

    def print_txt(self):
        """DOCSTRSINGS"""
        file_config_boot = open("config_boot.txt", 'r+')
        file_read_line = file_config_boot.readline()
        while file_read_line != "":
            print(file_read_line)
            file_read_line = file_config_boot.readline()
        file_config_boot.close()

    def read_config(self):
<<<<<<< HEAD
        m = open("config_boot.txt", 'r+')
        ar = m.readline()
        while ar != "":
            a = ar.split(" = ")
            if a[0] == "FIRMWARE":
                self.firmware = float(a[1])
            elif a[0] == "MODE":
                if a[1] == "True\n":
=======
        file_config_boot = open("config_boot.txt", 'r+')
        linea = file_config_boot.readline()
        while linea != "":
            split = linea.split(" = ")
            if split[0] == "FIRMWARE":
                # print(split[1])
                self.firmware = float(split[1])
                # print(self.firmware)
            elif split[0] == "MODE":
                if split[1] == "True\n":
>>>>>>> ba2436bf93881f03bb85bbd5c36ea9e33a0eeeaf
                    self.mode = True
                if split[1] == "False\n":
                    self.mode = False
<<<<<<< HEAD
            ar = m.readline()
        m.close()
=======
            linea = file_config_boot.readline()
            # print(self.mode)
            # print(self.firmware)
        file_config_boot.close()
>>>>>>> ba2436bf93881f03bb85bbd5c36ea9e33a0eeeaf
        self.print_txt()

    def run_user(self):
        """DOCSTRSINGS"""
        try:
            self.debug = debug_mode(True)  # True Or False
            self.wifi = WIFI(self.debug)
            self.mqtt = MQTT(self.debug)
            self.mqtt.client_mqtt.set_callback(self.callback)
            self.wifi.connect()
            self.mqtt.connect()
            self.cultivo = Cultivo(self.debug, self.mqtt)
            self.cultivo.read_sensores()
            self.cultivo.send_data()
            self.mqtt.add_topic(topic_key)
            count_time = 0
            while count_time < 20:
                sleep(1)
                count_time = count_time + 1
                self.mqtt.read()
            self.mqtt.disconnect()
            self.state()
        except:
            import machine
            machine.reset()

    def state(self):
        """DOCSTRSINGS"""
        try:
            if self.read[topic_key] == key:
                # if self.firmware< self
                self.set_mode(True)
                self.salvar_modo()
                print("Autorizado")  # Debug
        except:
<<<<<<< HEAD
            print("no boot")

    def save_file(self, name):
        self.sock = socket.socket()
        addr = socket.getaddrinfo(BROKER, 65)[0][-1]
        print(addr)
        self.sock.connect(addr)
        a = True
        f = open(name, "w")
        while a:
            try:
                res = self.sock.read(1024)
                if res != END_FILE:
                    f.write(res)
                elif res == END_FILE:
                    a = False
            except:
                print( "no data")
                break
        self.sock.close()
=======
            print("No boot")  # Debug
>>>>>>> ba2436bf93881f03bb85bbd5c36ea9e33a0eeeaf

    def callback(self, topic, msg):
        "Metodo que se ejcuta cuando llega un mensaje"
        print("LLEGO DATO")  # Debug
        self.read[topic] = msg
