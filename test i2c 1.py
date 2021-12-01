from machine import Pin
from machine import I2C
import time

sdaPIN = machine.Pin(0)
sclPIN = machine.Pin(1)

i2c = machine.I2C(0, sda = sdaPIN, scl = sclPIN ,freq =1700000)

devices = i2c.scan()

if len(devices) == 0:
    print ("no device")

for device in devices:
    print ("dec:", device, "hex:", hex(device))
#print (device)
#addr = device.to_bytes(1, 'little')
#print (addr)

#packageValue = 3

#package = packageValue.to_bytes(1, 'big')

#print (str(package))
#i2c.writeto(32, package)

#i2c.writeto(0x20,0x14)

#time.sleep(2)

#i2c.writeto_mem(32,20,package)

#hello world