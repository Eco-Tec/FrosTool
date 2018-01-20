from config import*
from MQTT import MQTT
from wifi import WIFI
from cultivo import Cultivo
from debug import debug_mode
#import machine
#import socket
import time
import socket

from umqtt.simple import MQTTClient


class Bootloader():
    def __init__(self):
        self.debug = ""
        self.wifi = ""
        self.mqtt = ""
        self.read = {}
        self.mode = False
        self.firmware = 1.0

        self.read_config()

    def run_boot(self):
        """Se entra en modo bootloader deacuerto a la solicitud del broker"""
        #self.read_config()
        if self.mode:
            print("modo boot")
            self.debug = debug_mode(True)  # True Or False
            self.wifi = WIFI(self.debug)
            self.wifi.connect()
            self.mqtt = MQTT(self.debug)
            self.mqtt.connect()
            self.mqtt.send_boot("/firmware/" + NAME, self.firmware)
            self.save_file("plantilla.txt")
            self.mqtt.disconnect()
        else:
            print("modo user")
            self.run_user()

    def set_firmware(self, version):
        self.firmware = version

    def set_mode(self, mode):
        self.mode = mode

    def salvar_modo(self):
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
        self.print_txt()

    def print_txt(self):
        a = open("config_boot.txt", 'r+')
        ar = a.readline()
        while ar != "":
            print(ar)
            ar = a.readline()
        a.close()

    def read_config(self):
        m = open("config_boot.txt", 'r+')
        ar = m.readline()
        while ar != "":
            a = ar.split(" = ")
            if a[0] == "FIRMWARE":
                self.firmware = float(a[1])
            elif a[0] == "MODE":
                if a[1] == "True\n":
                    self.mode = True
                if a[1] == "False\n":
                    self.mode = False
            ar = m.readline()
        m.close()
        self.print_txt()

    def run_user(self):
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
            a = 0
            while a < 20:
                time.sleep(1)
                a = a + 1
                self.mqtt.read()
            self.mqtt.disconnect()
            self.state()
        except:
            import machine
            machine.reset()

    def state(self):
        try:
            if self.read[topic_key] == key:
            #if self.firmware< self
                self.set_mode(True)
                self.salvar_modo()
                print ("autorizado")
        except:
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

    def callback(self, topic, msg):
        print("LLEGO DATO")
        self.read[topic]=msg
