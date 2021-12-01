from machine import Pin, I2C
from machine import ADC
import mcp23017
import time
i2c = I2C(0,scl=Pin(1), sda=Pin(0), freq =400000)
mcp = mcp23017.MCP23017(i2c, 0x20)

# variable declarations
Seg = 0
Module = 0
ModuleValue = 3
ResetPins = 0

# selects the Layer with the case statement, then checks wether the current led needs to be turned on.

def WriteToSeg(Value, ModuleNumber, ActiveLayer):
    if ActiveLayer == 0:
        if Value == 2 or Value == 3 or Value == 5 or Value == 7 or Value == 8 or Value == 9:
                mcp[ModuleNumber].output(0)
    elif ActiveLayer == 1:
        if Value == 1 or Value == 2 or Value == 3 or Value == 4 or Value == 5 or Value == 7 or Value == 8 or Value == 9:
                mcp[ModuleNumber].output(0)
    elif ActiveLayer == 2:
        if Value == 1 or Value == 3 or Value == 5 or Value == 6 or Value == 7 or Value == 8 or Value == 9:
                mcp[ModuleNumber].output(0)
    elif ActiveLayer == 3:
        if Value == 2 or Value == 3 or Value == 5 or Value == 6 or Value == 8 or Value == 9:
                mcp[ModuleNumber].output(0)
    elif ActiveLayer == 4:
        if Value == 2 or Value == 4 or Value == 6 or Value == 8:
                mcp[ModuleNumber].output(0)
    elif ActiveLayer == 5:
        if Value == 4 or Value == 5 or Value == 6 or Value == 8 or Value == 9:
                mcp[ModuleNumber].output(0)
    elif ActiveLayer == 6:
        if Value == 2 or Value == 3 or Value == 4 or Value == 5 or Value == 6 or Value == 8 or Value == 9:
                mcp[ModuleNumber].output(0)

#This is a complete clusterfuck, good luck to future me figuring this out.
while True:
    mcp[8].output(1)
    mcp[9].output(1)
    mcp[10].output(1)
    mcp[11].output(1)
    mcp[12].output(1)
    mcp[13].output(1)
    mcp[14].output(1)
    mcp[15].output(1)
    while Seg < 7:
        while Module < 16:
            mcp[Seg].output(0)
            WriteToSeg(ModuleValue, Module, Seg)
            mcp[Seg].output(1)
            Module += 1
        Module = 8
        Seg += 1
    Seg = 0


