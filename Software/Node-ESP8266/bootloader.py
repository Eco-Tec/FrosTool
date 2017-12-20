from config import*


from MQTT import MQTT
from wifi import WIFI
from cultivo import Cultivo
from debug import debug_mode
import machine



class Bootloader() :
    def __init__(self):


    def run_boot(self):
        rtc = machine.RTC()
        rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
        # Si el dispositivo desperto de el modo deep sleep
        if machine.reset_cause() == machine.DEEPSLEEP_RESET:
            # print('Desperto del modo deep sleep')  # Debug
            self.run_user()

        rtc.alarm(rtc.ALARM0, 10000)
        machine.deepsleep()


    def run_user(self):
        try:
            debug = debug_mode(True)  # True Or False
            wifi = WIFI(debug)
            mqtt = MQTT(debug)
            wifi.connect()
            cultivo = Cultivo(debug, mqtt)
            cultivo.read_sensores()
            cultivo.send_data()
        except:
            import machine
            machine.reset()
