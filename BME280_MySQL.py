import mysql.connector

import time
 
import board
import busio
import adafruit_bme280

i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

bme280.sea_level_pressure = 1013.25

while True:
        
    Temperatura = "%0.2f" % bme280.temperature
    Humedad = "%0.2f" % bme280.humidity
    Presion = "%0.2f" % bme280.pressure
    Altitud = "%0.2f" % bme280.altitude
    print ("\nTemperatura: " + Temperatura + " ºC")
    print ("Humedad: " + Humedad + " % H")
    print ("Presión: " + Presion + " hPa")
    print ("Altitud: " + Altitud + " metros")

    con = mysql.connector.connect(host='localhost', database='BME280', user='TU_USUARIO', password='TU_CONTRASEÑA')
    cursor= con.cursor()
    cursor.execute("INSERT INTO Valores (Temperatura, Humedad, Presion, Altitud) VALUES (%s, %s, %s, %s)" %(Temperatura, Humedad, Presion, Altitud))
    
    con.commit()
    cursor.close()
    con.close()
    time.sleep(60)