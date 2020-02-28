import network
import urequests

from secret import SSID, PASSWD

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(SSID, PASSWD)

while not station.isconnected():
    pass

response = urequests.get('http://jsonplaceholder.typicode.com/albums/1')
print(response.text)




