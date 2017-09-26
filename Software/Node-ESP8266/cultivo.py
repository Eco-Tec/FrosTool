from config import sens
from DHT22 import DHT22
import time


<<<<<<< HEAD
    def __init__(self,debug,mqtt):
        super(cultivo, self).__init__()
        self.mqtt=mqtt
        self.debug=debug
        self.sensores={}
        self.data={}
        #self.sensor=sens
=======
class Cultivo():

    def __init__(self, debug):
        super(Cultivo, self).__init__()
        self.debug = debug
        self.sensores = {}
        self.data = {}
        # self.sensor=sens
>>>>>>> a17a59d61b3dcceac05dbb0d18e313ff4902ddf8
        self.crear_cultivo()

    def crear_cultivo(self, sensor=sens):
        for i, n in sens.items():
            self.add_sensor(i, n)

    def add_sensor(self, name, tipo):
        if tipo == "DHT22":
            self.sensores[name] = DHT22(self.debug, name, pin_dht=4)

    def read_sensores(self):
        for i in sens:
            self.data[i] = self.sensores[i].readData()
            time.sleep_ms(500)
        self.debug.printDebug(self.data)

    def send_data(self):
        for i in sens:
            for n,m in self.data[i].items():
                self.mqtt.send(n,m)
                #self.debug.printDebug(n)
