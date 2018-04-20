from config import sensor_list
from DHT22 import DHT22


class Cultivo():
    "Clase que gestiona los datos del cultivo especifico"

    def __init__(self, debug):
        super(Cultivo, self).__init__()
        self.debug = debug
        self.sensores = {}
        self.data = {}
        # self.sensor=sensor_list
        self.init_RTC()
        self.crear_cultivo()

    def crear_cultivo(self, sensor=sensor_list):
        "Agrega los diferentes sensores del cultivo, "
        for nombre_s, tipo_s in sensor_list.items():
            self.add_sensor(nombre_s, tipo_s)

    def add_sensor(self, name, tipo):
        "instancia los diferentes tipos de sensor (Pines...)"
        if tipo == "DHT22":
            self.sensores[name] = DHT22(self.debug, name, pin_dht=4)

    def read_sensores(self):
        "Realiza la lectura de las variables fisicas de los diferentes tipos de sensores"
        for sensor in sensor_list:
            self.data[sensor] = self.sensores[sensor].readData()
        self.debug.printDebug("Conjunto de datos: ", self.data)  # Debug
        self.debug.visual()  # Debug

    def init_RTC(self):
        "Inicializa el hardware de reloj de tiempo real"
        try:
            from machine import Pin, I2C
            import ds1307  # File
            i2c = I2C(scl=Pin(0), sda=Pin(5), freq=100000)  # SCL-> GPIO0; SDA -> GPIO4
            if i2c.scan():
                self.ds = ds1307.DS1307(i2c)
                self.ds.datetime()  # Debug
            else:
                self.debug.printDebug("Error con el RTC: NO DETECTADO")  # Debug
        except Exception as error:
            self.debug.printDebug("Error con el RTC: ", error)  # Debug

    def saveData(self):
        "Guarda los datos en un archivo de texto plano con formato CSV"
        for sensor in sensor_list:
            humedad, name, temperatura = self.data[sensor].items()
            try:
                fecha = str(self.ds.datetime()[2]) + "/" + \
                    str(self.ds.datetime()[1]) + "/" + str(self.ds.datetime()[0])
                hora = str(self.ds.datetime()[4]) + ":" + \
                    str(self.ds.datetime()[5]) + ":" + str(self.ds.datetime()[6])
                self.f_cultivo = open('data.csv', 'a')
                self.f_cultivo.write(str(fecha) + ", " + str(hora) + ", " +
                                     str(temperatura[1]) + ", " + str(humedad[1]) + "\n")
                self.f_cultivo.close()
                self.debug.printDebug("Datos Guardados Correctamente\n")  # Debug
            except Exception as e:
                self.debug.printDebug("Problema Almacenando los datos. Error: ", e)  # Debug
