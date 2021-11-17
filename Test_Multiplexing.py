from machine import Pin, I2C
from machine import ADC
import mcp23017
import time
i2c = I2C(0,scl=Pin(1), sda=Pin(0))
mcp = mcp23017.MCP23017(i2c, 0x20)

# variable declarations
Seg = 0
Module = 0
ModuleValue = 0
ResetPins = 0

# selects the Layer with the case statement, then checks wether the current led needs to be turned on.

def WriteToSeg(Value, ModuleNumber, ActiveLayer):
    if ActiveLayer == 1:
        if Value == 2 or Value == 3 or Value == 5 or Value == 7 or Value == 8 or Value == 9:
                mcp[ModuleNumber].output(0)
    if ActiveLayer == 2:
        if Value == 1 or Value == 2 or Value == 3 or Value == 4 or Value == 5 or Value == 7 or Value == 8 or Value == 9:
                mcp[ModuleNumber].output(0)
    if ActiveLayer == 3:
        if Value == 1 or Value == 3 or Value == 5 or Value == 6 or Value == 7 or Value == 8 or Value == 9:
                mcp[ModuleNumber].output(0)
    if ActiveLayer == 4:
        if Value == 2 or Value == 3 or Value == 5 or Value == 6 or Value == 8 or Value == 9:
                mcp[ModuleNumber].output(0)
    if ActiveLayer == 5:
        if Value == 2 or Value == 4 or Value == 6 or Value == 8:
                mcp[ModuleNumber].output(0)
    if ActiveLayer == 6:
        if Value == 4 or Value == 5 or Value == 6 or Value == 8 or Value == 9:
                mcp[ModuleNumber].output(0)
    if ActiveLayer == 7:
        if Value == 2 or Value == 3 or Value == 4 or Value == 5 or Value == 6 or Value == 8 or Value == 9:
                mcp[ModuleNumber].output(0)

#This is  complete clusterfuck, good luck to future me figuring this out.
while True:
    while ModuleValue < 10:  
        print("Value", ModuleValue) 
        while ResetPins < 16:
            mcp[ResetPins].output(1)
            ResetPins += 1
        ResetPins = 0
        while Module < 16:
#            print("module", Module)
            while Seg < 8:
#                print("segment",Seg)
                mcp[Seg].output(0)
                WriteToSeg(ModuleValue, Module, Seg)
                mcp[Seg].output(1)
                Seg += 1
            Seg = 0
            Module += 1
        Module = 8
        ModuleValue += 1
    ModuleValue = 0