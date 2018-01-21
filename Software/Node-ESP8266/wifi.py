# imports hardware
# imports modulos
from config import SSID, PASSWORD
# imports library python
import time
# imports library Micro-python
import network


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
        self.intentos = 1
        self.t_reconect = 50  # Evaluar

    def connect(self, name=SSID, passw=PASSWORD):
        """Establece la conexión, recibe el nombre
           y clave de la red """
        while not self.sta_if.isconnected():
            self.intentos = 0
            self.sta_if.active(True)
            self.debug.printDebug('Conectando a la Red ...')
            self.sta_if.connect(name, passw)
            self.event()
        else:
            self.debug.printDebug({"Conexion establecida."})
            self.debug.visual()  # Debug

    def event(self):
        """ Rutina de reintento de reconexion,
            por cada intento duplica el tiempo de espera """
        #self.intentos = self.intentos + 1
        while not self.sta_if.isconnected():
            self.intentos = self.intentos + 1
            if self.intentos < 200:
                self.debug.printDebug("Intento de reconección No.", self.intentos)
                time.sleep_ms(self.t_reconect)
                self.status()
            else:
                self.disconnect()
                import machine
                machine.deepsleep()
        else:
            self.status()

    def disconnect(self):
        """Termina una conexión existente y deja
           disponble el modulo para Recibir otra conexion"""
        try:
            self.sta_if.disconnect()
        except:
            print("no desconectado")
        if self.sta_if.isconnected():
            try:
                self.sta_if.disconnect()
                self.sta_if.active(False)
                time.sleep_ms(1000)
            except Exception as error:
                self.event(self.status())
                self.debug.printDebugDebug(
                    {"Desconectado de la Red..."}, error)

    def status(self):
        """Determina el estado de la conexion y las posibles
           causas de errores"""
        self.debug.printDebug("\nEstado de conexion ...")
        self.debug.printDebug({'<-- Configuracion de la Red', self.sta_if.ifconfig()})
        self.debug.printDebug(str(self.estado[self.sta_if.status()]))
        #return(self.sta_if.status())
