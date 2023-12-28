from machine import Pin
import utime
from dataIns import Payload
#Defining pin outs
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
temp=[]
arr=[]

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
    
    def arrDistance(self):
        # export=timeSlot()
        arr.append(self.avgDistance())
        if len(arr)==self.freq+1:
            arr.clear()
        elif len(arr)==self.freq:
            return arr
        
class EventDecide:
    def __init__(self):
        self.arr=temp
        self.threshold=0
        currData=timeSlot(0.25)
        self.arr=currData.arrDistance()

    def EventPredict(self):
        if(self.arr):
            n=len(self.arr)
            self.threshold=self.arr[n-1]*.80
            if self.arr[0]<=self.threshold:
                # export=Payload(self.threshold)
                # res=export.insert()
                return "Event= drain",self.arr
            elif self.arr[0]>self.threshold:
                # export=Payload(self.threshold)
                # res=export.insert()
                return "Event = rise" ,self.arr


