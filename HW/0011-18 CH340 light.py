from machine import Pin
import time
#p2 = Pin(2, Pin.OUT)##2 is second pin          out-> output
#2 is second pin chip'import network
import time
import socket
from machine import Pin 
p2 = Pin(2, Pin.OUT) #LED
ap=network.WLAN(network.AP_IF)
ap.active(True)#default預設燈   out-> output
#p1 = Pin(1, Pin.OUT)#差GPIO5
print(" start ")
for i in range(1,10):
    p2.value(1) #  off
    #p1.value(0) # off
    time.sleep(1)
    p2.value(0) # on
    #p1.value(1) # on
    time.sleep(1)
p2.value(1)    #  off
#p1.value(0)    #  off
print(" end")