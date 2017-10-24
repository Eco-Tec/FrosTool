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
            self.debug.printDebug('Conectando a la Red ...')
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

    def disconnect(self):
        """Termina una conexión existente y deja
           disponble el modulo para Recibir otra conexion"""
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
        self.debug.printDebug({'Configuracion de la Red:', self.sta_if.ifconfig()})
        self.debug.printDebug(str(self.estado[self.sta_if.status()]))
        return(self.sta_if.status())
