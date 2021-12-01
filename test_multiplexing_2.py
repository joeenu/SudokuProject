from machine import Pin, I2C
from machine import ADC
import mcp23017
import time
i2c = I2C(0,scl=Pin(1), sda=Pin(0), freq =400000)
mcp = mcp23017.MCP23017(i2c, 0x20)


