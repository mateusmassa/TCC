# -*- coding: utf-8 -*-
import serial                          # carrega a biblioteca serial
import numpy                           # carrega a biblioteca numpy
import matplotlib.pyplot as plt        # carrega a biblioteca pyplot
import matplotlib.gridspec as gridspec # carrega a biblioteca gridspec
from drawnow import *                  # carrega a biblioteca drawnow

shearF = list()
normalF = list()
vertF = list()
horiF = list()


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

plt.ion()

cnt = 0

#fuction validationString
def validString(a):
    if (len(a) > 0):
        a = a.replace("\\n", "")
        a = a.replace("b'", "")
        a = a.replace("\\r","")
        aF = float(a.strip().replace(",", "."))
    return aF

#function makeFig()
def makeFig():
    
    gs = gridspec.GridSpec(ncols=2, nrows=2)
    
    #Plot 1
    plt.subplot(gs[0, 0])
    plt.ylim([-10, 0])
    plt.title('Shear Load')
    plt.grid(True)
    plt.ylabel('Shear Load [N]')
    #plt.xlabel('Sample no.')
    plt.plot(shearF, 'ro-', label='Shear')
    plt.legend(loc='upper left')
    
    #Plot 2
    plt.subplot(gs[0, 1])
    plt.ylim([-30, 0])
    plt.title('Normal Load')
    plt.grid(True)
    plt.ylabel('Normal Load [N]')
    #plt.xlabel('Sample no.')
    plt.plot(normalF, 'yo-', label='Normal')
    plt.legend(loc='upper left')
        
    #Plot 3
    plt.subplot(gs[1,0])
    plt.ylim([0.01, 0])
    plt.title('Vertical Displacement')
    plt.grid(True)
    plt.ylabel('Vert Displacement [mm]')
    plt.xlabel('Sample no.')
    plt.plot(vertF, 'bo-', label='Displacement V')
    plt.legend(loc='upper left')
    
    #Plot 4
    plt.subplot(gs[1,1])
    plt.ylim([-0.01, 0])
    plt.title('Horizontal Displacement')
    plt.grid(True)
    plt.ylabel('Horiz. Displacement [mm]')
    plt.xlabel('Sample no.')
    plt.plot(horiF, 'go-', label='Displacement H')
    plt.legend(loc='upper left')
    
    

# ----- main loop -----

while 1:
    
    ser0.write(b'R\r')
    a = ser0.readline()
    a = str(a)
    a = a[:-1]
        
    ser1.write(b'*1B1\r')
    b = ser1.readline()
    b = str(b)
    b = b[:-1]
    
    ser2.write(b'*1B1\r')
    c = ser2.readline()
    c = str(c)
    c = c[:-1]
    
    ser3.write(b'R\r')
    d = ser3.readline()
    d = str(d)
    d = d[:-1]
        
    if (len(a) > 0):
        shear =  b
        normal = c
        vert = a
        hori = d
                
        shearFloat = validString(shear)
        normalFloat = validString(normal)
        vertFloat = validString(vert)
        horiFloat = validString(hori)
        
        shearF.append(shearFloat)
        normalF.append(normalFloat)
        vertF.append(vertFloat)
        horiF.append(horiFloat)
        
        drawnow(makeFig)
        plt.pause(.000005)
        cnt = cnt + 1
        if(cnt > 20):
            shearF.pop(0)
            normalF.pop(0)
            vertF.pop(0)
            horiF.pop(0)
            
            #input("Aperte Enter para continuar: ")
        
    else:
        print("Aguardando entrada de dados!")       
