from grovepi import *
from grove_rgb_lcd import *
import time
from math import isnan
import sqlite3
from datetime import datetime


dht_sensor_port = 7

conn = sqlite3.connect('sensores.db')
cursor = conn.cursor()

while True:
    print("Leyendo sensor...")
    try:
        [temp, hum] = dht(dht_sensor_port, 0)  
        print("Resultado de dht():", [temp, hum])

        if not (isnan(temp) or isnan(hum)):
            print("Temp =", temp, "°C   Humidity =", hum, "%")

            t = round(temp, 1)
            h = round(hum, 1)

            setRGB(0, 255, 0)
            setText("Temp:" + str(t) + "C   " + "Humidity:" + str(h) + "%")

            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO lecturas (fecha, temperatura, humedad) VALUES (?, ?, ?)", (fecha, t, h))
            conn.commit()
            print("Datos guardados en la base de datos.")

        else:
            print("Datos no validos (NaN)")
            setRGB(255, 0, 0)
            setText("Sensor error")

    except (IOError, TypeError) as e:
        print("Error:", e)
        setRGB(255, 0, 0)
        setText("Read error")

    time.sleep(2)