from machine import Pin, I2C
import BME280
import network
import urequests
import socket
import esp

from page import web_page
from secret import SSID, PASSWD

esp.osdebug(None)

import gc

gc.collect()

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(SSID, PASSWD)

while not station.isconnected():
    pass

print('Connection successful')
print(station.ifconfig())

i2c = I2C(-1, scl=Pin(5), sda=Pin(4), freq=10000)

try:
    bme = BME280.BME280(i2c=i2c)
    temp = bme.temperature
    hum = bme.humidity
    pres = bme.pressure
    sensor_readings = {'temperature': temp, 'humidity': hum, 'pressure': pres}
    print(sensor_readings)
except OSError as e:
    print('Failed to read/publish sensor readings.')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('Content = %s' % request)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')
