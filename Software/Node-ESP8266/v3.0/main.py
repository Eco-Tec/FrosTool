from wifi import WIFI
from MQTT import MQTT

if __name__ == '__main__':
    mqtt=MQTT()
    wifi=WIFI()
    wifi.connect()
    mqtt.send("/cultivo/temp","data")
    mqtt.send("/cultivo/temp","data2")
    mqtt.send("/cultivo/temp","data4")
