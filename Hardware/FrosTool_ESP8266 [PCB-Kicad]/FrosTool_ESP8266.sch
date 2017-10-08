EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:ESP8266
LIBS:tp4056
LIBS:FrosTool_ESP8266-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 2
Title "PCB-Kicad FrosTool"
Date ""
Rev "1"
Comp "Eco-Tec"
Comment1 "@maurinc2010"
Comment2 "@fAndReS"
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L ESP-12E U?
U 1 1 59CAED20
P 5100 3650
F 0 "U?" H 5100 3550 50  0000 C CNN
F 1 "ESP-12E" H 5100 3750 50  0000 C CNN
F 2 "" H 5100 3650 50  0001 C CNN
F 3 "" H 5100 3650 50  0001 C CNN
	1    5100 3650
	1    0    0    -1  
$EndComp
$Comp
L AP1117-33 U?
U 1 1 59D43096
P 3250 1400
F 0 "U?" H 3100 1525 50  0000 C CNN
F 1 "AP1117-33" H 3250 1525 50  0000 L CNN
F 2 "TO_SOT_Packages_SMD:SOT-223-3Lead_TabPin2" H 3250 1600 50  0001 C CNN
F 3 "" H 3350 1150 50  0001 C CNN
	1    3250 1400
	1    0    0    -1  
$EndComp
$Comp
L Conn_01x01 J?
U 1 1 59D43147
P 9150 3350
F 0 "J?" H 9150 3450 50  0000 C CNN
F 1 "DATA_S1" H 9100 3250 50  0000 C CNN
F 2 "" H 9150 3350 50  0001 C CNN
F 3 "" H 9150 3350 50  0001 C CNN
	1    9150 3350
	1    0    0    -1  
$EndComp
Text Notes 9300 3050 0    60   ~ 0
SENSOR 1
$Comp
L C_Small C?
U 1 1 59D43D7C
P 2350 1500
F 0 "C?" H 2360 1570 50  0000 L CNN
F 1 "100nF" H 2360 1420 50  0000 L CNN
F 2 "" H 2350 1500 50  0001 C CNN
F 3 "" H 2350 1500 50  0001 C CNN
	1    2350 1500
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 59D446AA
P 3250 1800
F 0 "#PWR?" H 3250 1550 50  0001 C CNN
F 1 "GND" H 3250 1650 50  0000 C CNN
F 2 "" H 3250 1800 50  0001 C CNN
F 3 "" H 3250 1800 50  0001 C CNN
	1    3250 1800
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 59D446FE
P 9550 3650
F 0 "#PWR?" H 9550 3400 50  0001 C CNN
F 1 "GND" H 9450 3500 50  0000 C CNN
F 2 "" H 9550 3650 50  0001 C CNN
F 3 "" H 9550 3650 50  0001 C CNN
	1    9550 3650
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 59D4485B
P 6100 4050
F 0 "#PWR?" H 6100 3800 50  0001 C CNN
F 1 "GND" H 6100 3900 50  0000 C CNN
F 2 "" H 6100 4050 50  0001 C CNN
F 3 "" H 6100 4050 50  0001 C CNN
	1    6100 4050
	0    -1   -1   0   
$EndComp
$Comp
L CP C?
U 1 1 59D44B80
P 4100 1550
F 0 "C?" H 4125 1650 50  0000 L CNN
F 1 "10uF" H 4125 1450 50  0000 L CNN
F 2 "" H 4138 1400 50  0001 C CNN
F 3 "" H 4100 1550 50  0001 C CNN
	1    4100 1550
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR?
U 1 1 59D44DD9
P 4700 1400
F 0 "#PWR?" H 4700 1250 50  0001 C CNN
F 1 "+3.3V" H 4700 1540 50  0000 C CNN
F 2 "" H 4700 1400 50  0001 C CNN
F 3 "" H 4700 1400 50  0001 C CNN
	1    4700 1400
	0    1    1    0   
$EndComp
$Comp
L +3.3V #PWR?
U 1 1 59D45AA6
P 9800 3650
F 0 "#PWR?" H 9800 3500 50  0001 C CNN
F 1 "+3.3V" H 9700 3800 50  0000 C CNN
F 2 "" H 9800 3650 50  0001 C CNN
F 3 "" H 9800 3650 50  0001 C CNN
	1    9800 3650
	-1   0    0    1   
$EndComp
$Comp
L +3.3V #PWR?
U 1 1 59D45D80
P 4100 4050
F 0 "#PWR?" H 4100 3900 50  0001 C CNN
F 1 "+3.3V" H 4000 4200 50  0000 C CNN
F 2 "" H 4100 4050 50  0001 C CNN
F 3 "" H 4100 4050 50  0001 C CNN
	1    4100 4050
	0    -1   -1   0   
$EndComp
Text Label 8950 3350 2    60   ~ 0
DATA_S1
Text Label 6050 3550 0    60   ~ 0
DATA_S1
Text Notes 2250 850  0    60   ~ 0
POWER IN [Vin: 5.3V -> Vout 3.3V]
$Comp
L Conn_01x01 J?
U 1 1 59D47232
P 9150 4400
F 0 "J?" H 9150 4500 50  0000 C CNN
F 1 "DATA_S1" H 9100 4300 50  0000 C CNN
F 2 "" H 9150 4400 50  0001 C CNN
F 3 "" H 9150 4400 50  0001 C CNN
	1    9150 4400
	1    0    0    -1  
$EndComp
Text Notes 9300 4100 0    60   ~ 0
SENSOR 2
$Comp
L GND #PWR?
U 1 1 59D47241
P 9550 4700
F 0 "#PWR?" H 9550 4450 50  0001 C CNN
F 1 "GND" H 9450 4550 50  0000 C CNN
F 2 "" H 9550 4700 50  0001 C CNN
F 3 "" H 9550 4700 50  0001 C CNN
	1    9550 4700
	1    0    0    -1  
$EndComp
$Comp
L +3.3V #PWR?
U 1 1 59D47247
P 9800 4700
F 0 "#PWR?" H 9800 4550 50  0001 C CNN
F 1 "+3.3V" H 9700 4850 50  0000 C CNN
F 2 "" H 9800 4700 50  0001 C CNN
F 3 "" H 9800 4700 50  0001 C CNN
	1    9800 4700
	-1   0    0    1   
$EndComp
Text Label 8950 4400 2    60   ~ 0
DATA_S2
Text Notes 950  6300 0    60   ~ 0
TODO
Text Notes 1000 7050 0    60   ~ 0
GPIO16 -> Deep-sleep mode
Text Label 2350 1250 0    60   ~ 0
BAT+
Text Notes 1000 6550 0    60   ~ 0
ADC -> GPIO4
$Comp
L +3.3V #PWR?
U 1 1 59D48315
P 4100 3550
F 0 "#PWR?" H 4100 3400 50  0001 C CNN
F 1 "+3.3V" H 4000 3700 50  0000 C CNN
F 2 "" H 4100 3550 50  0001 C CNN
F 3 "" H 4100 3550 50  0001 C CNN
	1    4100 3550
	0    -1   -1   0   
$EndComp
Text Label 6050 3650 0    60   ~ 0
ADC_BAT
Text Label -850 5200 0    60   ~ 0
ADC_BAT
Text Label 6050 3750 0    60   ~ 0
DATA_S2
Text Label -2450 5200 2    60   ~ 0
BAT+
$Comp
L GND #PWR?
U 1 1 59D49172
P -1500 5350
F 0 "#PWR?" H -1500 5100 50  0001 C CNN
F 1 "GND" H -1500 5200 50  0000 C CNN
F 2 "" H -1500 5350 50  0001 C CNN
F 3 "" H -1500 5350 50  0001 C CNN
	1    -1500 5350
	1    0    0    -1  
$EndComp
Text Notes -2050 4900 0    60   ~ 0
VOLATGE DIVISOR
Text Notes 1000 7250 0    60   ~ 0
SENSOR ANALOG -> GPIO
Text Notes 1000 6650 0    60   ~ 0
MODO PROGRAMACION
NoConn ~ 4200 3450
NoConn ~ 4200 3650
NoConn ~ 4200 3750
NoConn ~ 4200 3850
NoConn ~ 4200 3950
NoConn ~ 6000 3950
NoConn ~ 4850 4550
NoConn ~ 4950 4550
NoConn ~ 5050 4550
NoConn ~ 5150 4550
NoConn ~ 5250 4550
NoConn ~ 5350 4550
$Comp
L USB_OTG J?
U 1 1 59D7F39A
P 13400 1700
F 0 "J?" H 13455 2167 50  0000 C CNN
F 1 "USB_OTG" H 13455 2076 50  0000 C CNN
F 2 "" H 13550 1650 50  0001 C CNN
F 3 "" H 13550 1650 50  0001 C CNN
	1    13400 1700
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 59D7F4E3
P 13400 2250
F 0 "#PWR?" H 13400 2000 50  0001 C CNN
F 1 "GND" H 13405 2077 50  0000 C CNN
F 2 "" H 13400 2250 50  0001 C CNN
F 3 "" H 13400 2250 50  0001 C CNN
	1    13400 2250
	1    0    0    -1  
$EndComp
Text GLabel 14000 1700 2    60   Input ~ 0
TXD
Text GLabel 14000 1800 2    60   Input ~ 0
RXD
Text GLabel 14000 1500 2    60   Input ~ 0
V5
$Comp
L CONN_01X02 J?
U 1 1 59D806A2
P 950 1500
F 0 "J?" H 869 1225 50  0000 C CNN
F 1 "IN_PANEL" H 869 1316 50  0000 C CNN
F 2 "" H 950 1500 50  0001 C CNN
F 3 "" H 950 1500 50  0001 C CNN
	1    950  1500
	-1   0    0    1   
$EndComp
Text GLabel 1300 1200 1    60   Input ~ 0
V5
$Comp
L CARGADOR U?
U 1 1 59D80E61
P 1650 1550
F 0 "U?" H 1725 1947 60  0000 C CNN
F 1 "CARGADOR" H 1725 1841 60  0000 C CNN
F 2 "" H 1650 1550 60  0001 C CNN
F 3 "" H 1650 1550 60  0001 C CNN
	1    1650 1550
	1    0    0    -1  
$EndComp
$Comp
L CONN_01X02 J?
U 1 1 59D80F79
P 2750 1950
F 0 "J?" H 2828 1991 50  0000 L CNN
F 1 "BATERIA" H 2828 1900 50  0000 L CNN
F 2 "" H 2750 1950 50  0001 C CNN
F 3 "" H 2750 1950 50  0001 C CNN
	1    2750 1950
	1    0    0    -1  
$EndComp
$Comp
L 2N3904 Q?
U 1 1 59D816D3
P -2350 3950
F 0 "Q?" H -2159 3996 50  0000 L CNN
F 1 "2N3904" H -2159 3905 50  0000 L CNN
F 2 "TO_SOT_Packages_THT:TO-92_Molded_Narrow" H -2150 3875 50  0001 L CIN
F 3 "" H -2350 3950 50  0001 L CNN
	1    -2350 3950
	1    0    0    -1  
$EndComp
$Comp
L 2N3904 Q?
U 1 1 59D817D6
P -850 3950
F 0 "Q?" H -659 3996 50  0000 L CNN
F 1 "2N3904" H -659 3905 50  0000 L CNN
F 2 "TO_SOT_Packages_THT:TO-92_Molded_Narrow" H -650 3875 50  0001 L CIN
F 3 "" H -850 3950 50  0001 L CNN
	1    -850 3950
	1    0    0    -1  
$EndComp
Text GLabel 1650 1950 3    60   Input ~ 0
LED1
Text GLabel 1850 1950 3    60   Input ~ 0
LED2
Wire Wire Line
	4200 4050 4100 4050
Wire Wire Line
	6100 4050 6000 4050
Wire Wire Line
	9600 3500 9600 3650
Wire Wire Line
	2350 1600 2350 1700
Wire Wire Line
	3250 1700 3250 1800
Connection ~ 2350 1700
Wire Wire Line
	3550 1400 4700 1400
Connection ~ 4100 1400
Connection ~ 3250 1700
Connection ~ 2350 1400
Wire Wire Line
	9600 3650 9550 3650
Wire Notes Line
	9000 3100 9000 3600
Wire Notes Line
	9000 3100 10000 3100
Wire Notes Line
	10000 3100 10000 3600
Wire Notes Line
	10000 3600 9000 3600
Wire Wire Line
	6050 3550 6000 3550
Wire Notes Line
	1150 950  5000 950 
Wire Notes Line
	5000 950  5000 2200
Wire Notes Line
	5000 2200 1150 2200
Wire Notes Line
	1150 2200 1150 950 
Wire Wire Line
	9600 4700 9550 4700
Wire Notes Line
	9000 4150 9000 4650
Wire Notes Line
	9000 4150 10000 4150
Wire Notes Line
	10000 4150 10000 4650
Wire Notes Line
	10000 4650 9000 4650
Wire Notes Line
	850  6350 5450 6350
Wire Notes Line
	5450 6350 5450 7600
Wire Notes Line
	5450 7600 850  7600
Wire Notes Line
	850  7600 850  6350
Wire Wire Line
	6050 3750 6000 3750
Wire Wire Line
	4200 3550 4100 3550
Wire Wire Line
	6050 3650 6000 3650
Wire Wire Line
	-850 5200 -950 5200
Wire Wire Line
	-2450 5200 -2200 5200
Wire Notes Line
	-2400 4950 -2400 5300
Wire Notes Line
	-2400 5300 -900 5300
Wire Notes Line
	-900 5300 -900 4950
Wire Notes Line
	-900 4950 -2400 4950
Wire Notes Line
	1000 6950 1150 6950
Wire Wire Line
	13400 2250 13400 2100
Wire Wire Line
	14000 1800 13700 1800
Wire Wire Line
	13700 1700 14000 1700
Wire Wire Line
	13300 2100 13300 2150
Wire Wire Line
	13300 2150 13400 2150
Connection ~ 13400 2150
Wire Wire Line
	14000 1500 13700 1500
Wire Wire Line
	2100 1400 2950 1400
Wire Wire Line
	2100 1650 2100 1700
Wire Wire Line
	2100 1700 4100 1700
Wire Wire Line
	2350 1250 2350 1400
Wire Wire Line
	1150 1450 1150 1400
Wire Wire Line
	1150 1400 1350 1400
Wire Wire Line
	1350 1650 1150 1650
Wire Wire Line
	1150 1650 1150 1550
Wire Wire Line
	1300 1200 1300 1400
Connection ~ 1300 1400
Wire Wire Line
	2550 1900 2550 1400
Connection ~ 2550 1400
Wire Wire Line
	2550 2000 2400 2000
Wire Wire Line
	2400 2000 2400 1700
Connection ~ 2400 1700
Wire Wire Line
	1850 1950 1850 1800
Wire Wire Line
	1650 1800 1650 1950
$Comp
L GND #PWR?
U 1 1 59D81C36
P -750 4250
F 0 "#PWR?" H -750 4000 50  0001 C CNN
F 1 "GND" H -745 4077 50  0000 C CNN
F 2 "" H -750 4250 50  0001 C CNN
F 3 "" H -750 4250 50  0001 C CNN
	1    -750 4250
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 59D81CD9
P -2250 4250
F 0 "#PWR?" H -2250 4000 50  0001 C CNN
F 1 "GND" H -2245 4077 50  0000 C CNN
F 2 "" H -2250 4250 50  0001 C CNN
F 3 "" H -2250 4250 50  0001 C CNN
	1    -2250 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	-2250 4250 -2250 4150
Wire Wire Line
	-750 4250 -750 4150
$Comp
L LED D?
U 1 1 59D81E6B
P -750 3500
F 0 "D?" V -712 3383 50  0000 R CNN
F 1 "LED" V -803 3383 50  0000 R CNN
F 2 "" H -750 3500 50  0001 C CNN
F 3 "" H -750 3500 50  0001 C CNN
	1    -750 3500
	0    -1   -1   0   
$EndComp
$Comp
L LED D?
U 1 1 59D81F6A
P -2250 3500
F 0 "D?" V -2212 3383 50  0000 R CNN
F 1 "LED" V -2303 3383 50  0000 R CNN
F 2 "" H -2250 3500 50  0001 C CNN
F 3 "" H -2250 3500 50  0001 C CNN
	1    -2250 3500
	0    -1   -1   0   
$EndComp
Wire Wire Line
	-2250 3750 -2250 3650
Wire Wire Line
	-750 3650 -750 3750
$Comp
L R R?
U 1 1 59D8213F
P -2250 3100
F 0 "R?" H -2180 3146 50  0000 L CNN
F 1 "R" H -2180 3055 50  0000 L CNN
F 2 "" V -2320 3100 50  0001 C CNN
F 3 "" H -2250 3100 50  0001 C CNN
	1    -2250 3100
	1    0    0    -1  
$EndComp
$Comp
L R R?
U 1 1 59D821C6
P -750 3100
F 0 "R?" H -680 3146 50  0000 L CNN
F 1 "R" H -680 3055 50  0000 L CNN
F 2 "" V -820 3100 50  0001 C CNN
F 3 "" H -750 3100 50  0001 C CNN
	1    -750 3100
	1    0    0    -1  
$EndComp
Wire Wire Line
	-750 3350 -750 3250
Wire Wire Line
	-2250 3250 -2250 3350
Text GLabel -750 2850 1    60   Input ~ 0
BAT+
Wire Wire Line
	-750 2850 -750 2950
Text GLabel -2250 2850 1    60   Input ~ 0
BAT+
Wire Wire Line
	-2250 2850 -2250 2950
$Comp
L R R?
U 1 1 59D82B55
P -1200 3950
F 0 "R?" V -1407 3950 50  0000 C CNN
F 1 "R" V -1316 3950 50  0000 C CNN
F 2 "" V -1270 3950 50  0001 C CNN
F 3 "" H -1200 3950 50  0001 C CNN
	1    -1200 3950
	0    1    1    0   
$EndComp
$Comp
L R R?
U 1 1 59D82C41
P -2700 3950
F 0 "R?" V -2907 3950 50  0000 C CNN
F 1 "R" V -2816 3950 50  0000 C CNN
F 2 "" V -2770 3950 50  0001 C CNN
F 3 "" H -2700 3950 50  0001 C CNN
	1    -2700 3950
	0    1    1    0   
$EndComp
Text GLabel -1450 3950 0    60   Input ~ 0
LED2
Wire Wire Line
	-1450 3950 -1350 3950
Text GLabel -2950 3950 0    60   Input ~ 0
LED1
Wire Wire Line
	-2950 3950 -2850 3950
$Comp
L 2N3904 Q?
U 1 1 59D831CB
P 6950 5650
F 0 "Q?" H 7141 5696 50  0000 L CNN
F 1 "2N3904" H 7141 5605 50  0000 L CNN
F 2 "TO_SOT_Packages_THT:TO-92_Molded_Narrow" H 7150 5575 50  0001 L CIN
F 3 "" H 6950 5650 50  0001 L CNN
	1    6950 5650
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR?
U 1 1 59D831D2
P 7050 5950
F 0 "#PWR?" H 7050 5700 50  0001 C CNN
F 1 "GND" H 7055 5777 50  0000 C CNN
F 2 "" H 7050 5950 50  0001 C CNN
F 3 "" H 7050 5950 50  0001 C CNN
	1    7050 5950
	1    0    0    -1  
$EndComp
Wire Wire Line
	7050 5950 7050 5850
$Comp
L LED D?
U 1 1 59D831D9
P 7050 5200
F 0 "D?" V 7088 5083 50  0000 R CNN
F 1 "LED" V 6997 5083 50  0000 R CNN
F 2 "" H 7050 5200 50  0001 C CNN
F 3 "" H 7050 5200 50  0001 C CNN
	1    7050 5200
	0    -1   -1   0   
$EndComp
Wire Wire Line
	7050 5350 7050 5450
$Comp
L R R?
U 1 1 59D831E1
P 7050 4800
F 0 "R?" H 7120 4846 50  0000 L CNN
F 1 "R" H 7120 4755 50  0000 L CNN
F 2 "" V 6980 4800 50  0001 C CNN
F 3 "" H 7050 4800 50  0001 C CNN
	1    7050 4800
	1    0    0    -1  
$EndComp
Wire Wire Line
	7050 5050 7050 4950
Text GLabel 7050 4550 1    60   Input ~ 0
BAT+
Wire Wire Line
	7050 4550 7050 4650
$Comp
L R R?
U 1 1 59D831EB
P 6600 5650
F 0 "R?" V 6393 5650 50  0000 C CNN
F 1 "R" V 6484 5650 50  0000 C CNN
F 2 "" V 6530 5650 50  0001 C CNN
F 3 "" H 6600 5650 50  0001 C CNN
	1    6600 5650
	0    1    1    0   
$EndComp
Wire Wire Line
	6350 5650 6450 5650
Wire Notes Line
	4300 4500 5950 4500
Wire Notes Line
	5950 4500 5950 2800
Wire Notes Line
	5950 2800 4300 2800
Wire Notes Line
	4300 2800 4300 4500
Text Notes 4900 2700 0    60   ~ 0
ESP8266
Text Label 6050 3350 0    60   ~ 0
TXD
Text Label 6050 3450 0    60   ~ 0
RXD
Wire Wire Line
	6000 3450 6050 3450
Wire Wire Line
	6000 3350 6050 3350
Wire Wire Line
	6000 3850 6050 3850
Text Label 6050 3850 0    60   ~ 0
DEBUG_LED
Text Label 6350 5650 2    60   ~ 0
DEBUG_LED
$Comp
L Conn_01x01 J?
U 1 1 59DA8FFF
P 9600 3300
F 0 "J?" H 9600 3400 50  0000 C CNN
F 1 "GND" V 9700 3350 50  0000 C CNN
F 2 "" H 9600 3300 50  0001 C CNN
F 3 "" H 9600 3300 50  0001 C CNN
	1    9600 3300
	0    -1   -1   0   
$EndComp
$Comp
L Conn_01x01 J?
U 1 1 59DA93EC
P 9750 3300
F 0 "J?" H 9750 3200 50  0000 C CNN
F 1 "V3.3" V 9850 3300 50  0000 C CNN
F 2 "" H 9750 3300 50  0001 C CNN
F 3 "" H 9750 3300 50  0001 C CNN
	1    9750 3300
	0    -1   -1   0   
$EndComp
Wire Wire Line
	9750 3500 9750 3650
Wire Wire Line
	9750 3650 9800 3650
$Comp
L Conn_01x01 J?
U 1 1 59DA9D39
P 9600 4350
F 0 "J?" H 9600 4450 50  0000 C CNN
F 1 "GND" V 9700 4400 50  0000 C CNN
F 2 "" H 9600 4350 50  0001 C CNN
F 3 "" H 9600 4350 50  0001 C CNN
	1    9600 4350
	0    -1   -1   0   
$EndComp
$Comp
L Conn_01x01 J?
U 1 1 59DA9D3F
P 9750 4350
F 0 "J?" H 9750 4250 50  0000 C CNN
F 1 "V3.3" V 9850 4350 50  0000 C CNN
F 2 "" H 9750 4350 50  0001 C CNN
F 3 "" H 9750 4350 50  0001 C CNN
	1    9750 4350
	0    -1   -1   0   
$EndComp
Wire Wire Line
	9600 4550 9600 4700
Wire Wire Line
	9750 4550 9750 4700
Wire Wire Line
	9750 4700 9800 4700
$Sheet
S 1700 2750 550  450 
U 59DAA3AB
F0 "TP4056" 60
F1 "TP4056.sch" 60
$EndSheet
$EndSCHEMATC
