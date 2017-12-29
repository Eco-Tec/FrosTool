from umqtt.simple import MQTTClient
# from ubinascii import hexlify
# from machine import unique_id
from config import *
from config import topico
import time

class MQTT():
    """Clase para gestionar la transmición y Recepcion de datos
       usando el protocolo MQTT"""

    def __init__(self, debug):
        super(MQTT, self).__init__()
        self.debug = debug
        # self.CLIENT_ID = hexlify(unique_id())
        self.CLIENT_ID = "NODO_2"
        self.list_topic = {}
        self.client_mqtt = MQTTClient(self.CLIENT_ID, BROKER)
        self.debug_mode = 1  # Debug On:1 | Off:0
        #self.client_mqtt.set_callback(self.callback)

    def add_topic(self, topic):
        self.list_topic[topic] = topic
        self.client_mqtt.subscribe(topic)

    #def callback(self, topic, msg):
    #    if topic==topic_boot:

            #print((topic, str(msg)))

    def connect(self):
        "Metodo que realiza la Conexion al protocolo MQTT"
        try:
            self.client_mqtt.connect()
            self.debug.printDebug("Conectando al Broker ....")
        except Exception as e:
            self.debug.printDebug({"Broker no disponble (Address, Service). "}, e)

    def disconnect(self):
        "Metodo que realiza la Desconexion al protocolo MQTT"
        try:
            self.client_mqtt.disconnect()
            self.debug.printDebug("Desconectado del Broker .....")
        except Exception as e:
            self.debug.printDebug({"Conexion MQTT no disponble ....."}, e)

    def send(self, topic, data, sensor):
        "Envio Datos mediante el protocolo MQTT"
        try:
            #self.connect()
            self.client_mqtt.publish(topic + topico + sensor, str(data))
            #self.disconnect()
            self.debug.printDebug({"Enviado dato ....", topic + topico, data})
            self.debug.visual()  # Debug
        except Exception as e:
            self.disconnect()
            self.debug.printDebug({"Fallo el envio de datos MQTT ....."}, e)

    def read(self):
        self.client_mqtt.check_msg()

    def subcribir(self):
        for i in self.list_topic:
            self.client_mqtt.subscribe(str(i))

    def send_boot(self, topic, data):
        self.client_mqtt.publish(topic, str(data))
