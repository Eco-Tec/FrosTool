import dht
import machine


class DHT22():
    "Clase padre, Monitoreo del dispositivo para micropython: "

    def __init__(self,debug, name ,pin_dht=4):
        self.debug=debug
        self.name=name
        self.temp=name+"/temp"
        self.hume=name+"/hum"
        self.pin_DHT = pin_dht
        self.s_dht = dht.DHT22(machine.Pin(self.pin_DHT))

    def readData(self):
        "Obtiene de los sensores los datos de Temperatura/Humedad"
        try:
            self.s_dht.measure()
            self.debug.print(self.name)
            self.debug.print(("Temperatura ", self.s_dht.temperature()))
            self.debug.print(("Humedad  ", self.s_dht.humidity()))
            return({self.temp:self.s_dht.temperature(),self.hume:self.s_dht.humidity()})
        except Exception as e:
            self.debug.print(("No fue posible la lectura de Datos error:", e))
