# -*- coding: utf-8 -*-
import serial
from time import sleep

# ----- Setup the Serial COM Port ------

ser = serial.Serial(
port='/dev/ttyUSB0',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

# ----- Read the Shear Load -----

while 1:
    ser.write('*1B1\n')
    x = ser.readline()
    x = x[:-1]
    x = x[:len(x)-1]
    a = len(x)
    print "\nShear load =",x
    print "\nTamanho =", a
    if (len(x) != 0):
        print "\nPrimeiro caracter =", x[0]
        print "\nUltimo caracter =", x[len(x)-1]
        b = float(x.strip().replace(",", "."))
        print "\nFloat =", b
    sleep(1)
