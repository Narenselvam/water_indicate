from machine import Pin
import utime
from dataIns import Payload
#Defining pin outs
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

temp=[]

class timeSlot:
    def __init__(self,freq=1):
        self.sec = 5
        self.freq=(freq*60)//5
        # print("The distance from object is ",self.distance,"cm")

    def getDistance(self):
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
        dist=Payload(distance)
        return distance

    def avgDistance(self): #currDsitamce
        avgDistance = 0
        for i in range(self.sec):
            avgDistance += self.getDistance()
            utime.sleep(1)
        avgDistance = avgDistance / self.sec
        dist=Payload(avgDistance)
        return avgDistance
        
class EventDecide:
    currData=timeSlot(2)
    

        


