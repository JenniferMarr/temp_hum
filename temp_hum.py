from grovepi import *
from grove_rgb_lcd import *
import time
from math import isnan

dth_sensor_port = 7

while True:
    try:
        [ temp, hum ] = dht(dth_sensor_port, 1)
        
        if not (isnan(temp) or isnan(hum)):
            print("Temp =", temp, "C\tHumidity =", hum, "%")
            
            t = round(temp, 1)
            h = round(hum, 1)
            
            setRGB(0, 255, 0)
            setText("Temp:" + str(t) + "C    Humidity:" + str(h) + "%")
        else:
            print("Datos no válidos (NaN)")
            setRGB(255, 0, 0)
            setText("Sensor error")
            
    except (IOError, TypeError) as e:
        print("Error", e)
        setRGB(255, 0, 0)
        setText("Read error")
    
    time.sleep(2)