from umqtt.simple import MQTTClient
#from ubinascii import hexlify
#from machine import unique_id
from config import BROKER
from config import topico


class MQTT():
    """Clase para gestionar la transmición y Recepcion de datos
       usando el protocolo MQTT"""

    def __init__(self, debug):
        super(MQTT, self).__init__()
        self.debug = debug
        #self.CLIENT_ID = hexlify(unique_id())
        self.CLIENT_ID = "NODO_2"
        self.client_mqtt = MQTTClient(self.CLIENT_ID, BROKER)
        self.debug_mode = 1  # Debug On:1 | Off:0
        self.client_mqtt.set_callback(self.callback)

    def callback(self, topic, msg):
        print(msg)

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

    def init_recivir(self):
        self.connect()
        #self.mqtt.subcribir("/firmware/key")
        self.client_mqtt.wait_msg()
        self.disconnect()


    def subcribir(self, topic):
        self.connect()
        #self.mqtt.subcribir("/firmware/key")
        self.client_mqtt.subscribe(topic)
        self.disconnect()

    def set_callback(self):
        print("Entro set_callback")

    def send_boot(self, topic, data):
        self.connect()
        self.client_mqtt.publish(topic, str(data))
        self.disconnect()

    def receive(self):
        "Metodo que recibe datos enviados a traves del protocolo MQTT"
        pass
