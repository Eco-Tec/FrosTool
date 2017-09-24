from umqtt.simple import MQTTClient
from ubinascii import hexlify
from machine import unique_id
from config import BROKER

class MQTT():
    """Clase para gestionar la transmición y Recepcion de datos
       usando el protocolo mqtt"""
    def __init__(self):
        super(MQTT, self).__init__()
        #self.arg = arg
        self.CLIENT_ID = hexlify(unique_id())
        self.client_mqtt = MQTTClient(self.CLIENT_ID, BROKER)

    def connect(self):
        try:
            self.client_mqtt.connect()
            print("Conectando al servidor ....")
        except:
            print("Servidor no disponble ....")

    def disconnect(self, arg):
        try:
            self.client_mqtt.disconnect()
            print("Desconectado del servidor .....")
        except:
            print("Conexion no disponble .....")

    def send(self, topic, data):
        try:
            print("Enviado dato ....")
            self.connect()
            self.client_mqtt.publish(topic, str(data))
            #self.disconnect()
        except Exception as e:
            self.disconnect()


    def receive(self, arg):
        pass
