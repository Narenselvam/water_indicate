import time
import network
import socket
import urequests as requests
from machine import Pin
import utime
from config import ssid, password,MONGO_API,API_KEY
from dataIns import currTime
# import zoneinfo
# #from DateTime import DateTime

#Defining pin outs
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)


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
    
    

def ultra():
 
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   currdist=currTime(distance)

   print("The distance from object is ",distance,"cm")

   url = MONGO_API
   headers = API_KEY

   print("sending...")

   response = requests.post(url, headers=headers, json=currdist.insert())

   print("Response: (" + str(response.status_code) + "), msg = " + str(response.text))

   if response.status_code == 201:
        print("Added Successfully")
   else:
       print("Error")
while True:
   ultra()
   utime.sleep(10)