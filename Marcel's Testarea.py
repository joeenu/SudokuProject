from Generator import *


solvedlist = [  "1","2","3","4","5","6","7","8","9",
                "9","1","2","3","4","5","6","7","8",
                "8","9","1","2","3","4","5","6","7",
                "7","8","9","1","2","3","4","5","6",
                "6","7","8","9","1","2","3","4","5",
                "5","6","7","8","9","1","2","3","4",
                "4","5","6","7","8","9","1","2","3",
                "3","4","5","6","7","8","9","1","2",
                "2","3","4","5","6","7","8","9","1"]

#print(solvedlist)


specifylist = [ "1","","3","4","5","6","7","8","9",
                "9","1","2","3","4","5","6","7","8",
                "8","9","1","2","3","4","5","6","7",
                "7","8","9","1","2","3","4","5","6",
                "6","7","8","9","1","2","3","4","5",
                "5","6","7","8","9","1","2","3","4",
                "4","5","6","7","8","9","1","2","3",
                "3","4","5","6","7","8","9","1","2",
                "2","3","4","5","6","7","8","9","1"]

#print(specifylist)


workinglist = [ "1","","3","4","5","6","7","8","9",
                "9","1","2","3","4","5","6","7","8",
                "8","9","1","2","3","4","5","6","7",
                "7","8","9","1","2","3","4","5","6",
                "6","7","8","9","1","2","3","4","5",
                "5","6","7","8","9","1","2","3","4",
                "4","5","6","7","8","9","1","2","3",
                "3","4","5","6","7","8","9","1","2",
                "2","3","4","5","6","7","8","9","1"]



segmentbutton = 1

numpadinput = 15

lastnumpad = 39

if len(specifylist[segmentbutton]) == 0:
    if numpadinput != 0:                            #funktioniert ned wenn s feld 3 bsp leer isch schribts dete nüt ine
        workinglist[segmentbutton] = numpadinput
        numpadinput = 0
    

print(workinglist)





difficulty = 40, 5 #da müend zwei variable ine wod schwirigkeit bestimmed. die 1. isch zum für schwirigkeitsgrad (höcher = schwieriger, 0-81) die zweit isch random schwirigkeit (ca 0 - 15)

gen = Generator("base.txt")

gen.randomize(100)

initial = gen.board.copy()

gen.reduce_via_logical(difficulty[0])

if difficulty[1] != 0:
    
    gen.reduce_via_random(difficulty[1])


final = gen.board.copy()

print("The initial board before removals was: \r\n\r\n{0}".format(initial))
print("The generated board after removals was: \r\n\r\n{0}".format(final))
print("")



final_string = format(final)

final_list = []
for i in final_string:
    if i == "_":
        final_list.append(0)
    elif i == "|":
        final_list.__delitem__
    elif i == "\r":
        final_list.__delitem__
    elif i == "\n":
        final_list.__delitem__
    else:
        final_list.append(int(i))

print(final_list)