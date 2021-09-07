# -*- coding: utf-8 -*-
import serial
from time import sleep

# ----- Setup the Serial COM Port ------

ser = serial.Serial(
port='/dev/ttyUSB3',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

# ----- Read the Shear Load -----

while 1:
    ser.write('R\r')
    x = ser.readline()
    x = x[:-1]                # Remove the last character	  
    print "Displacement =",x
    sleep(0.03)
