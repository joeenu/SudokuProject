#https://docs.micropython.org/en/latest/esp8266/tutorial/neopixel.html

import machine, neopixel
np = neopixel.NeoPixel(machine.Pin(0),567)

np[0] = (0,0,0)       #np[numere vo led] = (rot,grüen,blau)

np.write()              #mach das obedrah