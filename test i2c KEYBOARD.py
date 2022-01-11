from machine import Pin
from machine import I2C
import time


#define the rp2040 pin assignements
InterruptPin = machine.Pin(1, Pin.IN)
sdaPIN = machine.Pin(4)
sclPIN = machine.Pin(5)



#initialize the i2c connection
i2c = machine.I2C(0, scl=sclPIN, sda=sdaPIN, freq = 100000)


time.sleep(0.1)

#setup the ADP5587 keyboard controller.
i2c.writeto_mem(52,0x01, b'\x81')   #enables auto increment and the key events interrupt
i2c.writeto_mem(52,0x1d, b'\x1f')   #sets column 0 to 4 as part of the matrix
i2c.writeto_mem(52,0x1e, b'\x1f')   #sets row 0 to 4 as part of the matrix

while True:
    if not InterruptPin.value():
        InterruptActive = i2c.readfrom_mem(52, 3, 1)
        while InterruptAtive > 0:
            PressedKey = i2c.readfrom_mem(52, 4, 1)
            InterruptActive = i2c.readfrom_mem(52, 3, 1)
            print (PressedKey)
        i2c.writeto_mem(52,0x02, b'\x01')