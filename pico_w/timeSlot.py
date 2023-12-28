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
        
class defaultEvent:
    def __init__(self,n=0.25):
        self.arr=temp
        currData=timeSlot(n)
        self.arr=currData.arrDistance()

    def res_arr(self):
        return self.arr
    

class EventDecide:
    def __init__(self,n=0.25):
        self.threshold=0
        self.event=defaultEvent(n)

    def EventPredict(self):
        if(self.event.res_arr()):
            n=len(self.event.res_arr())
            self.threshold=self.event.res_arr()[n-1]*.80
            if self.event.res_arr()[0]<=self.threshold:
                # export=Payload(self.threshold)
                # res=export.insert()
                return "Event= drain",self.event.res_arr()
            elif self.event.res_arr()[0]>self.threshold:
                # export=Payload(self.threshold)
                # res=export.insert()
                return "Event= rise" ,self.arr


