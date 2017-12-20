from umqtt.simple import MQTTClient
from ubinascii import hexlify
from machine import unique_id
from config import BROKER
from config import topico


class MQTT():
    """Clase para gestionar la transmición y Recepcion de datos
       usando el protocolo MQTT"""

    def __init__(self, debug):
        super(MQTT, self).__init__()
        self.debug = debug
        self.CLIENT_ID = hexlify(unique_id())
        self.client_mqtt = MQTTClient(self.CLIENT_ID, BROKER)
        self.debug_mode = 1  # Debug On:1 | Off:0

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
            self.connect()
            self.client_mqtt.publish(topic + topico + sensor, str(data))
            self.disconnect()
            self.debug.printDebug({"Enviado dato ....", topic + topico, data})
            self.debug.visual()  # Debug
        except Exception as e:
            self.disconnect()
            self.debug.printDebug({"Fallo el envio de datos MQTT ....."}, e)

    def receive(self):
        "Metodo que recibe datos enviados a traves del protocolo MQTT"
        pass
