from config import sensor_list
from DHT22 import DHT22
from time import sleep_ms


class Cultivo():
    "Clase que gestiona los datos del cultivo especifico"

    def __init__(self, debug, mqtt):
        super(Cultivo, self).__init__()
        self.debug = debug
        self.mqtt = mqtt
        self.sensores = {}
        self.data = {}
        # self.sensor=sensor_list
        self.crear_cultivo()

    def crear_cultivo(self, sensor=sensor_list):
        "Agrega los diferentes sensores del cultivo, "
        for nombre_s, tipo_s in sensor_list.items():
            self.add_sensor(nombre_s, tipo_s)

    def add_sensor(self, name, tipo):
        "instancia los diferentes tipos de sensor (Pines...)"
        if tipo == "DHT22":
            self.sensores[name] = DHT22(self.debug, name, pin_dht=4)

    def read_sensores(self):
        "Realzia la lectura de las variables fisicas de los diferentes tipos de sensores"
        for sensor in sensor_list:
            self.data[sensor] = self.sensores[sensor].readData()
        self.debug.printDebug(self.data)

    def send_data(self):
        "Envia los datos de los diferentes sensores haciendo uso del protocolo MQTT"
        for sensor in sensor_list:
            for topic, data in self.data[sensor].items():
                self.mqtt.send(topic, data)
                # self.debug.printDebug(topic)
