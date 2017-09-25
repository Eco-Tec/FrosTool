import dht
import machine


class DHT22():
    "Clase padre, Monitoreo del dispositivo para micropython: "

    def __init__(self, pin_dht=4):
        self.pin_DHT = pin_dht
        self.s_dht = dht.DHT22(machine.Pin(self.pin_DHT))
        self.debug_mode = 1  # Debug On:1 | Off:0

    def readData(self):
        "Obtiene de los sensores los datos de Temperatura/Humedad"
        try:
            self.s_dht.measure()
            return str(self.s_dht.temperature()), str(self.s_dht.humidity())
            if self.debug_mode == 1:
                print("Temperatura ", self.s_dht.temperature())  # Debug
                print("Humedad  ", self.s_dht.humidity())  # Debug
                self.pin_led_debug.value(not self.pin_led_debug.value())  # Debug visual
        except Exception as e:
            if self.debug_mode == 1:
                print("No fue posible la lectura de Datos error:", e)
            else:
                pass

    def debugMode(self, mode=0):
        "Activa/Desactiva El debug visual y de consola serial, On:1 | Off:0"
        import machine
        self.debug_mode = mode
        if self.debug_mode == 1:
            self.pin_led_debug = machine.Pin(2, machine.Pin.OUT)  # Debug visual
