#wichtig und bruchts
from Generator import *
from machine import Pin
import machine, neopixel, os, rp2, array, time


'''
#Generator shit
#----------------------------------------------------------------------------------------
difficulty = 40, 5 #da müend zwei variable ine wod schwirigkeit bestimmed. die 1. isch zum für schwirigkeitsgrad (höcher = schwieriger, 0-81) die zweit isch random schwirigkeit (ca 0 - 15)
gen = Generator("base.txt")
gen.randomize(100)
initial = gen.board.copy()
gen.reduce_via_logical(difficulty[0])
if difficulty[1] != 0:
    gen.reduce_via_random(difficulty[1])
final = gen.board.copy()


#löscht unnötiges züg us de final-lischte
final_string = format(final)
final_list = []
for i in final_string:
    if i == "_":
        final_list.append(str(0))
    elif i == "|":
        final_list.__delitem__
    elif i == "\r":
        final_list.__delitem__
    elif i == "\n":
        final_list.__delitem__
    else:
        final_list.append(i)


#löscht unnötiges züg us de initial-lischte
initial_string = format(initial)
initial_list = []
for i in initial_string:                            
    if i == "|":
        initial_list.__delitem__
    elif i == "\r":
        initial_list.__delitem__
    elif i == "\n":
        initial_list.__delitem__
    else:                                           
        initial_list.append(i)
'''

final_list =   ["2", "4", "6", "0", "0", "0", "0", "0", "0",
                "0", "0", "0", "9", "8", "7", "2", "6", "0",
                "8", "0", "0", "6", "0", "0", "1", "0", "3",
                "6", "0", "0", "0", "3", "2", "0", "0", "8",
                "3", "2", "1", "0", "0", "0", "6", "0", "5",
                "0", "0", "7", "4", "6", "0", "3", "0", "0",
                "5", "0", "3", "0", "0", "0", "7", "8", "0",
                "0", "1", "0", "0", "0", "9", "0", "0", "0",
                "0", "9", "0", "3", "5", "6", "0", "2", "0"]

initial_list = ["2", "4", "6", "5", "1", "3", "8", "9", "7",
                "1", "3", "5", "9", "8", "7", "2", "6", "4",
                "8", "7", "9", "6", "2", "4", "1", "5", "3",
                "6", "5", "4", "1", "3", "2", "9", "7", "8",
                "3", "2", "1", "7", "9", "8", "6", "4", "5",
                "9", "8", "7", "4", "6", "5", "3", "1", "2",
                "5", "6", "3", "2", "4", "1", "7", "8", "9",
                "4", "1", "2", "8", "7", "9", "5", "3", "6",
                "7", "9", "8", "3", "5", "6", "4", "2", "1"]



# Configure the number of WS2812 LEDs.
NUM_LEDS =567
PIN_NUM = 0
brightness = 0.1

@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

def changeLights(arr):
    # Create the StateMachine with the ws2812 program, outputting on pin
    sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

    # Start the StateMachine, it will wait for data on its FIFO.
    sm.restart()
    sm.active(1)

    # sm.put(array.array("I", [(r<<16) + (g<<8) + b for _ in range(567)]),8)
    sm.put(array.array("I", arr),8)


# def ledval(r, g, b):
#     return (r << 16) + (g << 8) + b

#def updateLED(arr):
#    global sm
#    print("hello")
#    
#    print("world")

#ordned d lischte nomal neu so dasmer die für leds bruche chan
ledsegmentorder =   [8,7,6,5,4,3,2,1,0,
                    9,10,11,12,13,14,15,16,17,
                    26,25,24,23,22,21,20,19,18,
                    27,28,29,30,31,32,33,34,35,
                    44,43,42,41,40,39,38,37,36,
                    45,46,47,48,49,50,51,52,53,
                    62,61,60,59,58,57,56,55,54,
                    63,64,65,66,67,68,69,70,71,
                    80,79,78,77,76,75,74,73,72,]


solved_list = [initial_list[i] for i in ledsegmentorder]

edit_list = [final_list[i] for i in ledsegmentorder] #das chönti falsch sii                       !!!!!!!!!!
#------------------------------------------------------------------------------------------------
print(edit_list)

#Chnöpflishit
#------------------------------------------------------------------------------------------------
inputpins = []
outputpins = []

C0 = Pin(2, Pin.OUT)
outputpins.append(C0)
C1 = Pin(3, Pin.OUT)
outputpins.append(C1)
C2 = Pin(4, Pin.OUT)
outputpins.append(C2)
C3 = Pin(5, Pin.OUT)
outputpins.append(C3)
C4 = Pin(6, Pin.OUT)
outputpins.append(C4)
C5 = Pin(7, Pin.OUT)
outputpins.append(C5)
C6 = Pin(8, Pin.OUT)
outputpins.append(C6)
C7 = Pin(9, Pin.OUT)
outputpins.append(C7)
C8 = Pin(10, Pin.OUT)
outputpins.append(C8)

R0 = Pin(11, Pin.IN)
inputpins.append(R0)
R1 = Pin(12, Pin.IN)
inputpins.append(R1)
R2 = Pin(13, Pin.IN)
inputpins.append(R2)
R3 = Pin(14, Pin.IN)
inputpins.append(R3)
R4 = Pin(15, Pin.IN)
inputpins.append(R4)
R5 = Pin(16, Pin.IN)
inputpins.append(R5)
R6 = Pin(17, Pin.IN)
inputpins.append(R6)
R7 = Pin(18, Pin.IN)
inputpins.append(R7)
R8 = Pin(19, Pin.IN)
inputpins.append(R8)

#das isch für numpad
R9 = Pin(20, Pin.IN)


def Index_button(outputpins, inputpins):
    while True:
        for outputpin, o_pin_num in enumerate(outputpins):
            # print(outputpin, o_pin_num)
            o_pin_num.value(1)
            # print([inputpin.value() for inputpin in inputpins])
            for inputpin, i_pin_num in enumerate(inputpins):
                if i_pin_num.value() == 1:
                    o_pin_num.value(0)
                    if outputpin % 2 != 0:
                        edit_list[outputpin*10 - inputpin + 7 + (int(outputpin/2)-1)*-2 -2] = "10"
                        return outputpin*10 - inputpin + 7 + (int(outputpin/2)-1)*-2 -2
                    else:
                        edit_list[outputpin*9 + inputpin] = "10"
                        return outputpin*9 + inputpin
            o_pin_num.value(0)

def Numpad_button(inputpins):
    print("Checking Numpad buttons")
    while True:
        for outputpin, o_pin_num in enumerate(outputpins):
            print(outputpin)
            o_pin_num.value(1)
            print(R9.value())
            if R9.value() == 1:
                o_pin_num.value(0)
                return outputpin
            else:
                o_pin_num.value(0)
            
""" def Numpad_button(inputpins):
    print("Checking Numpad buttons")
    while True:
        print([inputpin.value() for inputpin in inputpins])
        R9.value(1)
        for inputpin, i_pin_num in enumerate(inputpins):
            print(inputpin, i_pin_num)
            if i_pin_num.value() == 1:
                return inputpin """
#------------------------------------------------------------------------------------------------






#LED-shit
#------------------------------------------------------------------------------------------------
#wievill vo dene dinger ahghänkt sind
np = neopixel.NeoPixel(machine.Pin(0),567)
#Liste welli LEDs für welli Zahl muess lüchte
LED_for_num = {
    "0":[0,0,0,0,0,0,0],
    "1":[0,0,1,0,0,1,0],
    "2":[1,0,1,1,1,0,1],
    "3":[1,0,1,1,0,1,1],
    "4":[0,1,1,1,0,1,0],
    "5":[1,1,0,1,0,1,1],
    "6":[1,1,0,1,1,1,1],
    "7":[1,0,1,0,0,1,0],
    "8":[1,1,1,1,1,1,1],
    "9":[1,1,1,1,0,1,1],
    "10":[1,1,1,1,1,1,1],
}

def Switch_LED(LED_index, state):
    np.write(f"{LED_index} {state}")   #da s print zu dem ändere wo de output wiitergit

def Update_LEDs(list):
    arr = []
    for grid_index, num in enumerate(list):                     #gaht dur jedi Zahl vom Sudoku
        for segment_index, state in enumerate(LED_for_num[num]):#gaht dur jedes LED vom Segment
            LED_index = grid_index*7 + segment_index            #berechnet die gnau LED position
#            Switch_LED(LED_index, state)                        #füehrt für jedes LED de Command us
            if state == 1:
                if num == "10":
                    arr.append((0<<16) + (0<<8) + 10)
                else:
                    arr.append((10<<16) + (0<<8) + 0)
            else:
                arr.append((0<<16) + (0<<8) + 0)

    notComplete = False
    for i in list:
        if i == "0":
            notComplete = True
    if notComplete == False:
        arr = [(100<<16) + (100<<8) + 100 for _ in range(567)]

    changeLights(arr)
    # print(arr)
#------------------------------------------------------------------------------------------------




#de grossi loop
#------------------------------------------------------------------------------------------------

print(solved_list)

while edit_list != solved_list:
    Update_LEDs(edit_list)
    # print(edit_list)
    segmentbutton = Index_button(outputpins, inputpins)
    # print(segmentbutton)
    Update_LEDs(edit_list)
    if edit_list[segmentbutton] == "10":
        edit_list[segmentbutton] = str(Numpad_button(inputpins)+1)
        
#------------------------------------------------------------------------------------------------




#ab da bisch fertig
#------------------------------------------------------------------------------------------------
print("GG ez")
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------






#TESTAREA
#------------------------------------------------------------------------------------------------
#sötti d farbe vo de LEDs ändere (wiis = vorgäh; blau = selber inegsetzt)


#muess obe nach "edit_list = [final_list[i] for i in ledsegmentorder]" ine
'''
early_edit_list = edit_list
'''

#muess obe bi "def Update_LEDs" gänderet werde
'''
def Update_LEDs(list):
    for grid_index, num in enumerate(list):                     #gaht dur jedi Zahl vom Sudoku
        for segment_index, state in enumerate(LED_for_num[num]):#gaht dur jedes LED vom Segment
            LED_index = grid_index*7 + segment_index            #berechnet die gnau LED position
            Switch_LED(LED_index, state)                        #füehrt für jedes LED de Command us
            if state == 1 and segment_index in early_edit_list != "0":
                np[LED_index] = (150,150,150)
                np.write()
            elif state == 1 and segment_index in early_edit_list == "0":
                np[LED_index] = (20,20,150)
                np.write()
            else:
                np[LED_index] = (0,0,0)
                np.write()
'''
