from type_sensor import*

CONFIG = b""
PIN_ALARMA = 17
PIN_STOP_ALARMA = 4
SET_TEMP = 0
SET_HUM = 80



BROKER = {"DEVICE": "ORANGE_PI", "ADRESS": "192.168.0.16",
          "NAME_NETWORK": "FrosTool", "PASSWORD": "Password_de_paso", "NUMBER_BROKER": "1.0", "LOCATION": "5.7180354, -72.9244577"}

CULTIVO = {"TIPO_CULTIVO": "UVAS", "NAME_FINCA": "LA MORITA", "LOCATION": "5.7180354, -72.9244577"}


NODO_NORTE = {"SENSOR_1": DTH22, "SENSOR_2" : DTH22 ,"LOCATION": "5.7180354, -72.9244577"}

              
         
NODO_SUR = {"SENSOR_1": DTH22, "SENSOR_2" : DTH22 , "LOCATION": "5.7180354, -72.9244577" }



LIST_SENSOR = {"NODO_1" : NODO_NORTE, "NODO_2" : NODO_SUR}
#TOPICOS = {"TEMPERATURA": b"/CULTIVO/TEMP", "HUMEDAD": b"/CULTIVO/HUM", "ALARMA": b"/CULTIVO/ALARMA"}






