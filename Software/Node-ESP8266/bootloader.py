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


class Bootloader():
    def __init__(self):
        self.debug = ""
        self.wifi = ""
        self.mqtt = ""
        self.read = {}
        self.mode = False
        self.firmware = 1.0
        # self.config_boot = open("config_boot.txt", 'r+')
        # self.read_config()

    def run_boot(self):
        """Modo bootloader dada la solicitud del broker"""
        self.read_config()
        if self.mode:
            print("modo boot")  # Debug
            self.debug = debug_mode(True)  # True Or False
            self.wifi = WIFI(self.debug)
            self.wifi.connect()
            try:
                if self.wifi.sta_if.isconnected():
                    self.mqtt = MQTT(self.debug)
                    self.mqtt.connect()
                    self.mqtt.send_boot("/firmware/" + NAME, self.firmware)
                    self.mqtt.disconnect()
            except OSError:
                import machine
                machine.reset()
        else:
            self.run_user()

    def set_firmware(self, version):
        """DOCSTRSINGS"""
        self.firmware = version

    def set_mode(self, mode):
        """DOCSTRSINGS"""
        self.mode = mode

    def salvar_modo(self):
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
                    self.mode = True
                if split[1] == "False\n":
                    self.mode = False
            linea = file_config_boot.readline()
            # print(self.mode)
            # print(self.firmware)
        file_config_boot.close()
        self.print_txt()
        #self.firmware =self.firmware + 0.1
        # print(self.firmware)

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
            print("No boot")  # Debug

    def callback(self, topic, msg):
        "Metodo que se ejcuta cuando llega un mensaje"
        print("LLEGO DATO")  # Debug
        self.read[topic] = msg
