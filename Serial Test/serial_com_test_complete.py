# -*- coding: utf-8 -*-
import serial
from time import sleep

# ----- Setup the Serial COM Port ------

ser0 = serial.Serial(
port='/dev/ttyUSB0',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

ser1 = serial.Serial(
port='/dev/ttyUSB1',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

ser2 = serial.Serial(
port='/dev/ttyUSB2',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

ser3 = serial.Serial(
port='/dev/ttyUSB3',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

# ----- Print header -----

print "\n-------------------------------------------------------------------"
print "   Shear Load   |   Normal Load   |   Vert. Disp   |   Horiz. Disp "
print "-------------------------------------------------------------------"

# ----- Loop -----
while 1:
    a = ""
    b = ""
    c = ""
    d = ""    
    
    ser0.write('R\r')
    a = ser0.readline()
    a = a[:-1]
    a = a[0] + a[4:]
    
    sleep(0.1)
    
    ser1.write('*1B1\r')
    b = ser1.readline()
    b = b[:-1]
    b = b[0] + b[4:]
    
    sleep(0.1)
    
    ser2.write('*1B1\r')
    c = ser2.readline()
    c = c[:-1]
    c = c[0] + c[3:]
    
    sleep(0.1)
    
    ser3.write('R\r')
    d = ser3.readline()
    d = d[:-1]
    d = d[0] + d[4:]
    
    sleep(0.1)
    
     
    print ("      {}             {}            {}".format(b, c, a))
    
    sleep(1.6)
    
    a = ""
    b = ""
    c = ""
    d = ""