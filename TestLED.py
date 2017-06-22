from GPIO import GPIO
import time

x = GPIO(69)

x.openPin()
x.setDirection("out")

x.setValue(1)
time.sleep(.5)
x.setValue(0)
time.sleep(.5)
x.setValue(1)
time.sleep(.5)
x.setValue(0)

x.closePin()
