import time
import network
import socket
import urequests as requests
from machine import Pin
import utime
from config import ssid, password,MONGO_API,API_KEY
from timeSlot import timeSlot
# import zoneinfo
# #from DateTime import DateTime

#Initialing WLAN
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)


# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
    
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    
# arr=[]
time=5


def ultra():
        url = MONGO_API
        headers = API_KEY
        print("sending...")
        export=timeSlot()
        res=export.arrDistance()
        if res:
            print(res)
        # response = requests.post(url, headers=headers, json=export.getDistance())

        # print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))

        # if response.status_code == 201:
        #         print("Added Successfully")
        # else:
        #     print("Error")
while True:
   ultra()
   #utime.sleep(10)