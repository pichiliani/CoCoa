from GPIO import GPIO
import time

x = GPIO(36)

x.openPin()

x.setDirection("in")

print  x.getValue()

x.closePin()



#x = GP.getPin(36)

#print x.getValue()
#print x.getDirection()

#
#print x.getDirection()
#for i in range(0,9):
#    x.high()
    #print x.getValue()
#    time.sleep(.5)
#    x.low()
    #print x.getValue()
#    time.sleep(.5)



#GP.cleanup()
