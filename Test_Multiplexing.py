from machine import Pin, I2C
from machine import ADC
import mcp23017
import time
i2c = I2C(0,scl=Pin(1), sda=Pin(0))
mcp = mcp23017.MCP23017(i2c, 0x20)

# defining the pins each segment is connected to
Seg0 = 00
Seg1 = 00
Seg2 = 00
Seg3 = 00
Seg4 = 00
Seg5 = 00
Seg6 = 00
Seg7 = 00


# selects the Layer with the case statement, then checks wether the current led needs to be turned on.

def WriteToSeg(SegValue, SegPin, ActiveLayer):
    match ActiveLayer:
        case 1:
            if SegValue == 2 or 3 or 5 or 7 or 8 or 9:
                mcp[SegPin].output(0)
        case 2:
            if SegValue == 1 or 2 or 3 or 4 or 5 or 7 or 8 or 9:
                mcp[SegPin].output(0)
        case 3:
            if SegValue == 1 or 3 or 5 or 6 or 7 or 8 or 9:
                mcp[SegPin].output(0)
        case 4:
            if SegValue == 2 or 3 or 5 or 6 or 8 or 9:
                mcp[SegPin].output(0)
        case 5:
            if SegValue == 2 or 4 or 6 or 8:
                mcp[SegPin].output(0)
        case 6:
            if SegValue == 4 or 5 or 6 or 8 or 9:
                mcp[SegPin].output(0)
        case 7:
            if SegValue == 2 or 3 or 4 or 5 or 6 or 8 or 9:
                mcp[SegPin].output(0)


