# imports hardware
# imports modulos
from config import NAME, key, BROKER, END_FILE
from cultivo import Cultivo
from MQTT import MQTT
from wifi import WIFI
from debug import debug_mode
from config import SSID, PASSWORD
# imports library python
import network
# imports library python
from time import sleep
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
            print("modo boot")  # Debug
            #self.debug = debug_mode(True)  # True Or False
            #self.wifi = WIFI(self.debug)
            #self.wifi.connect()
            self.wifi_init()
            self.wifi_connect()
            self.sock = socket.socket()
            self.addr = socket.getaddrinfo(BROKER, 45)[0][-1]
            print(self.addr)
            #self.mqtt = MQTT(self.debug)
            #self.mqtt.connect()
            self.sock.connect(self.addr)
            self.sock.send("/firware/"+ str(NAME))
            #self.mqtt.send_boot("/firmware/" + NAME, self.firmware)
            #self.save_file("plantilla.txt")
            #self.mqtt.disconnect()
        else:
            print("modo user")
            self.run_user()

    def wifi_init(self):
        self.estado = {0: 'no connection and no activity', 1: 'connecting in progress',
                       2: 'failed due to incorrect password', 3: 'failed because no access point replied',
                       4: 'failed due to other problems', 5: 'connection successful', 255: ""}
        self.sta_if = network.WLAN(network.STA_IF)
        # self.ap_if =WLAN(network.AP_IF)
        self.intentos = 1
        self.t_reconect = 50  # Evalua

    def wifi_connect(self, name=SSID, passw=PASSWORD):
        """Establece la conexión, recibe el nombre
           y clave de la red """
        while not self.sta_if.isconnected():
            self.intentos = 0
            self.sta_if.active(True)
            print('Conectando a la Red ...')
            self.sta_if.connect(name, passw)
            self.wifi_event()
        else:
            print("Conexion establecida.")
            #self.debug.visual()  # Debug

    def wifi_event(self):
        """ Rutina de reintento de reconexion,
            por cada intento duplica el tiempo de espera """
        while not self.sta_if.isconnected():
            self.intentos = self.intentos + 1
            if self.intentos < 200:
                #print("Intento de reconección No.", self.intentos)
                time.sleep_ms(self.t_reconect)
                #self.status()
            else:
                self.wifi_disconnect()
                import machine
                machine.deepsleep()
        else:
            print(str(self.estado[self.sta_if.status()]))

    def wifi_disconnect(self):
        """Termina una conexión existente y deja
           disponble el modulo para Recibir otra conexion"""
        try:
            self.sta_if.disconnect()
        except:
            print("no desconectado")




    def set_firmware(self, version):
        """DOCSTRSINGS"""
        self.firmware = version

    def set_mode(self, mode):
        """DOCSTRSINGS"""
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
        """DOCSTRSINGS"""
        file_config_boot = open("config_boot.txt", 'r+')
        file_read_line = file_config_boot.readline()
        while file_read_line != "":
            print(file_read_line)
            file_read_line = file_config_boot.readline()
        file_config_boot.close()

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
            self.wifi.disconnect()
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
            print("no boot")

    def save_file(self, name):
        self.sock.connect(self.addr)
        a = True
        f = open(name, "w")
        while a:
            res = self.sock.readline().decode()
            if res == "END_FILE\n":
                print("sale")
                a = False
            else:
                f.write(res)
        self.sock.close()
        f.close()

    def callback(self, topic, msg):
        "Metodo que se ejcuta cuando llega un mensaje"
        print("LLEGO DATO")  # Debug
        self.read[topic] = msg
