import esp
from umqtt.simple import MQTTClient


class debug_mode():
    """Clase usada para gestionar el modo debug"""

    def __init__(self, modo=False):
        super(debug_mode, self).__init__()
        self.modo = modo
        self.set_modo(self.modo)

    def active(self):
        "Activa / Desactiva El debug visual y de consola serial(UART0)
        esp.osdebug(False)
        self.client_mqtt.DEBUG = False
        print("Modo debug activado ...")

    def desactive(self):
        """Desactive debug"""
        print("Modo debug desactivado ....")
        esp.osdebug(0)
        self.client_mqtt.DEBUG = True

    def printDebug(self, msm):
        """Envia mensajes por debug si esta activado"""
        if self.modo:
            print(str(msm))

    def set_modo(self, modo):
        """Cambia el modo de debug"""
        self.modo = modo
        if not modo:
            self.desactive()
        else:
            self.active()

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
