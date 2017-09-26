import time
import network
from config import SSID, PASSWORD


class WIFI():
    """Clase para conexion y desconexion del modulo de la red wifi"""

    def __init__(self, debug):
        super(WIFI, self).__init__()
        self.debug = debug
        self.estado = {0: 'no connection and no activity', 1: 'connecting in progress',
                       2: 'failed due to incorrect password', 3: 'failed because no access point replied',
                       4: 'failed due to other problems', 5: 'connection successful', 255: ""}
        self.sta_if = network.WLAN(network.STA_IF)
        # self.ap_if =WLAN(network.AP_IF)
        self.intentos = 0
        self.disconnect()
        self.sta_if.active(False)

    def connect(self, name=SSID, passw=PASSWORD):
        """Establece la conexión, recibe el nombre
           y clave de la red """
        if not self.sta_if.isconnected():
            self.intentos = 0
            self.debug.printDebug('Connecting to network...')
            self.sta_if.active(True)
            self.sta_if.connect(name, passw)
            time.sleep_ms(5000)
            self.event(self.status())

    def event(self, a):
        """Se encarga del numero de intentos para realziar la reconexion"""
        self.intentos = self.intentos + 1
        if a == 1 and self.intentos < 6:
            time.sleep_ms(5000)
            self.event(self.status())

            # self.connect()
        # elif a==2:
        #    print(str(self.estado[a]))
        # else:
        #    print(str(self.estado[a]))
            #print("Error desconocido")

    def disconnect(self):
        """Termina una conexión existente y deja
           disponble el modulo para resivir otra conexion"""
        if self.sta_if.isconnected():
            try:
                self.sta_if.disconnect()
                self.sta_if.active(False)
                time.sleep_ms(1000)
            except Exception as e:
                self.event(self.status())
                self.debug.printDebugDebug("Desconectado de la Red...")

    def status(self):
        """Determina el estado de la conexion y las posibles
           causas de errores"""
        self.debug.printDebug("Estado de conexion ....")
        self.debug.printDebug({'network config:', self.sta_if.ifconfig()})
        self.debug.printDebug(str(self.estado[self.sta_if.status()]))
        return(self.sta_if.status())

#    def debugMode(self, mode=0):
#        "Activa/Desactiva El debug visual y de consola serial, On:1 | Off:0"
#        self.debug_mode = mode
#        import esp
#        if self.debug_mode == 1:
#            esp.osdebug(0)  # redirect vendor O/S debugging messages to UART(0)
#        else:
#            esp.osdebug(None)
