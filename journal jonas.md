17.11.21
Setup of Programming enviroment and GIT project.
Setup of board design software.

24.11.21
Research into possible and available IC's to use in the project, defining of technical specifications of the project.

1.12.21
confirming of theoretical compatability of all seleced components.
ordering of selected components

15.12.21
creating testing methods and programming them.

22.12.21
Testing of i^2c device compatability with MAX6955 LED-driver.
tesing results:     device does not acknowledge the incominge communicaion from the master device.
problem:            device does not perform the Pulldown of the ACK bit expected by the protocol.
conclusion:         not able to get devive to work. the use of 7-Seg LED modules is impossibl wihout a driver ic, du to io limitations.
                    switching display method to individually adressable WS2812B-2020 "neopixel" LED's

christmas break:
Testing of i^2c device compaability with ADP5587 Mobile I/O Expander and QWERTY Keypad Controller.
testing results:    device connects, and can be written to without prolem, 4.7k pullup resistors needed on both lines to create a cleaner signal.
                    upon addessing the device to be read from, the connection seems to stop working.
problem:            upon receiving the read address, the device does not let go of the SDA line after the ACK bit, locking the bus until power is cycled.
conclusion:         while writing to the device is possible, reading from t produces a error. could not find source of problem, but could hav something to do with 
                    a NACK bug when the first bit to be read is a 0. switching to directly connecting th keyboard to the RP2040 mirocontroller. this increases the program and board comlexity, wich is why we tried to avoid it.

12.1.22
Creating the PCB schematic for the LED-string, the built in buttons and power delivery.

12.1.22
transferring components to PCB dsign and beginning of routing.

19.1.22
Routing of the pcb

26.1.22
finishing routing, and confirming of all specifications

2.2.22
starting with the documentation.

17.-19.2.22
Soldering of the PCB, testing of the LEDs
more work on the documentation

20.-25.2.22 
finishing the documentation
