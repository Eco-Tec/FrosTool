import network
from config import SSID, PASSWORD
import time


class WIFI():
    """Clase para conexion y desconexion del modulo de la red wifi"""

    def __init__(self):
        super(WIFI, self).__init__()
        # self.arg = arg
        self.estado = {0: 'no connection and no activity', 1: 'connecting in progress',
                       2: 'failed due to incorrect password', 3: 'failed because no access point replied',
                       4: 'failed due to other problems', 5: 'connection successful', 255: ""}
        self.sta_if = network.WLAN(network.STA_IF)
        # self.ap_if =WLAN(network.AP_IF)
        self.disconnect()
        self.sta_if.active(False)

    def connect(self, name=SSID, passw=PASSWORD):
        """Establece la conexion, recibe el nombre
           y clave de la red """

        if not self.sta_if.isconnected():
            print('connecting to network...')
            self.sta_if.active(True)
            self.sta_if.connect(name, passw)
            m = 0
            time.sleep_ms(5000)
            self.event(self.status())
        else:
            self.status()

    def event(self, a):
        if a == 1:
            time.sleep_ms(5000)
            self.event(self.status())
            # self.connect()
        # elif a==2:
        #    print(str(self.estado[a]))
        # else:
        #    print(str(self.estado[a]))
            #print("Error desconocido")

    def disconnect(self):
        """Termina una conexión existente y dejas
           disponble el modulo para reciver orta conexion"""
        if self.sta_if.isconnected():
            print("Deconectado de network ....")
            self.sta_if.disconnect()
            self.sta_if.active(False)
            time.sleep_ms(1000)
            self.status()
        else:
            print("No esta conectado al network ...")

    def status(self):
        """Determina el estado de la conexion y las posibles
           causa de errores"""
        print("Estado de conexion ....")
        print('network config:', self.sta_if.ifconfig())
        print(str(self.estado[self.sta_if.status()]))
        return(self.sta_if.status())
