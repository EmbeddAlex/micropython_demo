from machine import Pin, I2C
import BME280
import network
import socket
import gc

from page import web_page

gc.enable()
station = network.WLAN(network.AP_IF)
station.active(True)
station.config(authmode=0, essid='MicroPython')

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
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Got a connection from {}'.format(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        conn.send(b'HTTP/1.1 200 OK\n')
        conn.send(b'Content-Type: text/html\n')
        conn.send(b'Connection: close\n\n')
        conn.sendall(web_page(bme))
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')
