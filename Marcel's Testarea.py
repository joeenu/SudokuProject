#wichtig und bruchts
from os import write
from Generator import *
from machine import Pin
import machine, neopixel



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


#Chnöpflishit
#------------------------------------------------------------------------------------------------
inputpins = []

C0 = Pin(4, Pin.OUT)
inputpins.append(C0)
C1 = Pin(5, Pin.OUT)
inputpins.append(C1)
C2 = Pin(6, Pin.Out)
inputpins.append(C2)
C3 = Pin(7, Pin.Out)
inputpins.append(C3)
C4 = Pin(9, Pin.Out)
inputpins.append(C4)
C5 = Pin(10, Pin.Out)
inputpins.append(C5)
C6 = Pin(11, Pin.Out)
inputpins.append(C6)
C7 = Pin(12, Pin.Out)
inputpins.append(C7)
C8 = Pin(14, Pin.Out)
inputpins.append(C8)

outputpins = []

R0 = Pin(15, Pin.IN)
inputpins.append(R0)
R1 = Pin(16, Pin.IN)
inputpins.append(R1)
R2 = Pin(17, Pin.IN)
inputpins.append(R2)
R3 = Pin(19, Pin.IN)
inputpins.append(R3)
R4 = Pin(20, Pin.IN)
inputpins.append(R4)
R5 = Pin(21, Pin.IN)
inputpins.append(R5)
R6 = Pin(22, Pin.IN)
inputpins.append(R6)
R7 = Pin(24, Pin.IN)
inputpins.append(R7)
R8 = Pin(25, Pin.IN)
inputpins.append(R8)

#das isch für numpad
R9 = Pin(26, Pin.IN)


def Index_button(outputpins, inputpins):
    while True:
        for outputpin, o_pin_num in enumerate(outputpins):
            outputpin.value(1)
            for inputpin, i_pin_num in enumerate(inputpins):
                if inputpin == 1:
                    return o_pin_num*9 + i_pin_num


def Numpad_button(inputpins):
    while True:
        R9.value(1)
        for inputpin, i_pin_num in enumerate(inputpins):
            if inputpin == 1:
                return i_pin_num
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
}

def Switch_LED(LED_index, state):
    np.write(f"{LED_index} {state}")   #da s print zu dem ändere wo de output wiitergit

def Update_LEDs(list):
    for grid_index, num in enumerate(list):                     #gaht dur jedi Zahl vom Sudoku
        for segment_index, state in enumerate(LED_for_num[num]):#gaht dur jedes LED vom Segment
            LED_index = grid_index*7 + segment_index            #berechnet die gnau LED position
            Switch_LED(LED_index, state)                        #füehrt für jedes LED de Command us
            if state == 1:
                np[LED_index] = (150,150,150)
                np.write()
            else:
                np[LED_index] = (0,0,0)
                np.write()
#------------------------------------------------------------------------------------------------




#de grossi loop
#------------------------------------------------------------------------------------------------

print(solved_list)

while edit_list != solved_list:

    print(edit_list)

    segmentbutton = Index_button(outputpins, inputpins)

    if edit_list[segmentbutton] == "0":
        edit_list[segmentbutton] = str(Numpad_button()+1)

    Update_LEDs(edit_list)
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
