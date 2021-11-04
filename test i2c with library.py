from machine import Pin, I2C
import mcp23017
import time
i2c = I2C(0,scl=Pin(1), sda=Pin(0))
mcp = mcp23017.MCP23017(i2c, 0x20)

devices = i2c.scan()

for device in devices:
    print ("dec:", device, "hex:", hex(device))

#mcp.gpio = 0x0001
while False:
    mcp[8].output(1)
    time.sleep(0.5)
    mcp[9].output(1)
    mcp[8].output(0)
    time.sleep(0.5)
    mcp[9].output(0)

mcp.gpio = 0