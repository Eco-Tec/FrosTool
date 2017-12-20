import dht
import machine


class DHT22():
    "Clase referente solo al sensor DHT22 (Pines, topicos, lectura de datos)"

    def __init__(self, debug, name, pin_dht=4):
        self.debug = debug
        self.name = name
        self.temp = "/UVAS/Temp"
        self.hume = "/UVAS/Hum"
        self.pin_DHT = pin_dht
        self.s_dht = dht.DHT22(machine.Pin(self.pin_DHT))

    def readData(self):
        "Obtiene de los sensores los datos de Temperatura/Humedad"
        try:
            self.s_dht.measure()
            self.debug.printDebug(self.name)
            self.debug.printDebug(("Temperatura ", self.s_dht.temperature()))  # Debug
            self.debug.printDebug(("Humedad  ", self.s_dht.humidity()))  # Debug
            return({self.temp: self.s_dht.temperature(), self.hume: self.s_dht.humidity(), "name": self.name})
        except Exception as e:
            self.debug.printDebug(("No fue posible la lectura de Datos error:", e))  # Debug
