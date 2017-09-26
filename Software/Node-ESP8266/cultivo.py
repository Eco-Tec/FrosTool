from config import sens
from config import topico
from DHT22 import DHT22
import time

class cultivo():

    def __init__(self,debug):
        super(cultivo, self).__init__()
        self.debug=debug
        self.sensores={}
        self.data={}
        #self.sensor=sens
        self.crear_cultivo()

    def crear_cultivo(self,sensor=sens):
        for i,n in sens.items():
            self.add_sensor(i,n)

    def add_sensor(self, name,tipo):
        if tipo=="DHT22":
            self.sensores[name]=DHT22(self.debug,name,pin_dht=4)

    def read_sensores(self):
        for i in sens:
            self.data[i]=self.sensores[i].readData()
            time.sleep_ms(500)
        self.debug.print(self.data)

    def send_data(self):
        pass
