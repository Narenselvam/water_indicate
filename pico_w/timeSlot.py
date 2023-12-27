from machine import Pin
import utime
from dataIns import Payload
#Defining pin outs
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)


class timeSlot:
    def __init__(self,sec):
        self.sec = sec
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
        self.distance = (timepassed * 0.0343) / 2
        print("The distance from object is ",self.distance,"cm")

    def getDistance(self):
        dist=Payload(self.distance)
        return dist.insert()

    def avgDistance(self):
        avgDistance = 0
        for i in range(self.sec):
            avgDistance += self.getDistance()
        avgDistance = avgDistance / self.sec
        dist=Payload(avgDistance)
        return dist.insert()
        