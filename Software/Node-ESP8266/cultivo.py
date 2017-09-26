from config import sens
from DHT22 import DHT22
import time


class Cultivo():
    "Clase que gestiona los datos del cultivo especifico"

    def __init__(self, debug, mqtt):
        super(Cultivo, self).__init__()
        self.debug = debug
        self.mqtt = mqtt
        self.sensores = {}
        self.data = {}
        # self.sensor=sens
        self.crear_cultivo()

    def crear_cultivo(self, sensor=sens):
        "Agrega los diferentes sensores del cultivo, "
        for i, n in sens.items():
            self.add_sensor(i, n)

    def add_sensor(self, name, tipo):
        "instancia los diferentes tipos de sensor (Pines...)"
        if tipo == "DHT22":
            self.sensores[name] = DHT22(self.debug, name, pin_dht=4)

    def read_sensores(self):
        "Realzia la lectura de las variables fisicas de los diferentes tipos de sensores"
        for i in sens:
            self.data[i] = self.sensores[i].readData()
            time.sleep_ms(500)
        self.debug.printDebug(self.data)

    def send_data(self):
        "Envia los datos de los diferentes sensores haciendo uso del protocolo MQTT"
        for i in sens:
            for n, m in self.data[i].items():
                self.mqtt.send(n, m)
                # self.debug.printDebug(n)
