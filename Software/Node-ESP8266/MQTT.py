import time
from umqtt.simple import MQTTClient
from ubinascii import hexlify
from machine import unique_id
from config import BROKER


class MQTT():
    """Clase para gestionar la transmición y Recepcion de datos
       usando el protocolo MQTT"""

    def __init__(self,debug):
        super(MQTT, self).__init__()
        self.debug=debug
        self.CLIENT_ID = hexlify(unique_id())
        self.client_mqtt = MQTTClient(self.CLIENT_ID, BROKER)
        self.debug_mode = 1  # Debug On:1 | Off:0

    def connect(self):
        "Metodo que realiza la Conexion al protocolo MQTT"
        try:
            self.client_mqtt.connect()
            self.debug.print("Conectando al servidor ....")
        except Exception as e:
            self.debug.print({"Servidor no disponble ....", e})

    def disconnect(self):
        "Metodo que realiza la Desconexion al protocolo MQTT"
        try:
            self.client_mqtt.disconnect()
            self.debug.print("Desconectado del servidor .....")
        except Exception as e:
            self.debug.print({"Conexion no disponble .....",e})

    def send(self, topic, data):
        "Envio Datos mediante el protocolo MQTT"
        try:
            self.connect()
            self.client_mqtt.publish(topic, str(data))
            self.disconnect()
            time.sleep_ms(200)
            self.debug.print({"Enviado dato ....", topic, data})
        except Exception as e:
            self.disconnect()
            self.debug.print({"Fallo el envio de datos MQTT .....", e})

    def receive(self):
        "Metodo que recibe datos enviados a traves del protocolo MQTT"
        pass

#    def debugMode(self, mode=0):
#        "Activa/Desactiva El debug visual y de consola serial, On:1 | Off:0"
#        import esp
#        import machine
#        self.debug_mode = mode
#        if self.debug_mode == 1:
#            esp.osdebug(0)  # redirect vendor O/S debugging messages to UART(0)
#            self.pin_led_debug = machine.Pin(2, machine.Pin.OUT)  # Debug visual
#            self.client_mqtt.DEBUG = True
#        else:
#            esp.osdebug(None)
#            self.client_mqtt.DEBUG = False
