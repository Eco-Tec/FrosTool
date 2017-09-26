from config import sensores
from DHT22 import DHT22

class cultivo():

    def __init__(self,debug):
        super(cultivo, self).__init__()
        self.debug=debug
        self.senores={}
        self.data={}
        self.sensor=sensores

    def crear_cultivo(self,sensor=sensores):
        for i,n in sensor.items():
            self.add_sensor(i,n)


    def add_sensor(self, name,tipo):
        if tipo=="DHT22":
            self.sensor[name]=DHT22(name)


    def read_sensores(self):
        pass

    def send_data(self):
        password
