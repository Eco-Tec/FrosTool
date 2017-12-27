from config import*


from MQTT import MQTT
from wifi import WIFI
from cultivo import Cultivo
from debug import debug_mode
import machine

import socket
import time



class Bootloader() :
    def __init__(self):
        self.debug = ""
        self.wifi = ""
        self.mqtt = ""

        self.mode = False
        self.firmware = 1.0
        self.config_boot = open ("config_boot.txt", 'r+')
        #self.read_config()

    def run_boot(self):
        """Se entra en modo bootloader deacuerto a la solicitud del broker"""
        self.read_config()
        print(self.mode)
        if self.mode:
            #mqtt.send_boot("/firmware/" + NAME, FIRMWARE)
            self.debug = debug_mode(True)  # True Or False
            self.wifi = WIFI(self.debug)
            self.mqtt = MQTT(self.debug)
            self.wifi.connect()
            print("MODO BOOT")
            self.mqtt.send_boot("/firmware/" + NAME, self.firmware)
            self.mqtt.subcribir("/firmware/key")
            a=0
            while a < 100:
                time.sleep(1)
                a = a + 1
                print("halo")
                self.mqtt.init_recivir()
                print("halo 2")
            #time.sleep(10)
        else:
            self.run_user()

        #print(self.firmware)
    #def subribir_firmware(self):
    #    self.mqtt.subcribir("/firmware/key")

    def recive_firmware(self):
        pass

    def set_firmware(self, version):
        self.firmware = version

    def set_mode(self, mode):
        self.mode = mode

    def salvar_modo(self):
        a = open ("config_boot.txt", 'r+')
        ar= a.readline()
        while ar !="":
            am = ar.split(" = ")
            if am[0] == "FIRMWARE":
                a.write("FIRMWARE = "+ str(self.firmware)+'\n')
            elif am[0]== "MODE" :
                a.write("MODE = "+ str(self.mode)+'\n')
            ar= a.readline()
        a.close()

    def read_config(self):
        ar= self.config_boot.readline()
        while ar !="":
            a = ar.split(" = ")
            if a[0] == "FIRMWARE":
                #print(a[1])
                self.firmware = float (a[1])
                #print(self.firmware)
            elif a[0]== "MODE":
                if a[1]== "True\n":
                    self.mode =True
                if a[1]== "False\n":
                    self.mode =False
            ar= self.config_boot.readline()
            #print(self.mode)
            #print(self.firmware)
        self.config_boot.close()
        #self.firmware =self.firmware + 0.1
        #print(self.firmware)

    def run_user(self):
        try:
            debug = debug_mode(True)  # True Or False
            wifi = WIFI(debug)
            mqtt = MQTT(debug)
            wifi.connect()
            cultivo = Cultivo(debug, mqtt)
            cultivo.read_sensores()
            cultivo.send_data()
        except:
            import machine
            machine.reset()
