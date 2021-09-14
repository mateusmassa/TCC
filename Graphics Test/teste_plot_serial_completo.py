# -*- coding: utf-8 -*-
import serial                          # carrega a biblioteca serial
from time import sleep                 # carrega a biblioteca time
import numpy                           # carrega a biblioteca numpy
import matplotlib.pyplot as plt        # carrega a biblioteca pyplot
import matplotlib.gridspec as gridspec # carrega a biblioteca gridspec
from drawnow import *                  # carrega a biblioteca drawnow
from array import array                # carrega a biblioteca array

# ----- Setup the Serial COM Port ------
arduinoData = serial.Serial( port='/dev/ttyUSB0', baudrate = 9600, parity=serial.PARITY_NONE, 
                             stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

shearF = list()
normalF = list()
vertF = list()
horiF = list()

plt.ion()

cnt = 0

#fuction validationString
def validString(a):
    if (len(a) > 0):
        a = a.replace("b'", " ")
        aF = float(a.strip().replace(",", "."))
    return aF

#function makeFig()
def makeFig():
    
    gs = gridspec.GridSpec(ncols=2, nrows=2)
    
    #Plot 1
    plt.subplot(gs[0, 0])
    plt.ylim([0,40])
    plt.title('Shear Load')
    plt.grid(True)
    plt.ylabel('Shear Load [N]')
    #plt.xlabel('Sample no.')
    plt.plot(shearF, 'ro-', label='Shear')
    plt.legend(loc='upper left')
    
    #Plot 2
    plt.subplot(gs[0, 1])
    plt.ylim([0,10])
    plt.title('Normal Load')
    plt.grid(True)
    plt.ylabel('Normal Load [N]')
    #plt.xlabel('Sample no.')
    plt.plot(normalF, 'yo-', label='Normal')
    plt.legend(loc='upper left')
        
    #Plot 3
    plt.subplot(gs[1,0])
    plt.ylim([0,3])
    plt.title('Vertical Displacement')
    plt.grid(True)
    plt.ylabel('Vert Displacement [mm]')
    plt.xlabel('Sample no.')
    plt.plot(vertF, 'bo-', label='Displacement V')
    plt.legend(loc='upper left')
    
    #Plot 4
    plt.subplot(gs[1,1])
    plt.ylim([0,3])
    plt.title('Horizontal Displacement')
    plt.grid(True)
    plt.ylabel('Horiz. Displacement [mm]')
    plt.xlabel('Sample no.')
    plt.plot(horiF, 'go-', label='Displacement H')
    plt.legend(loc='upper left')
    
    

# ----- main loop -----

while 1:
    
    arduinoData.write(b'*1B1\n')
    data = arduinoData.readline()
    data = str(data)
    data = data[:-1]
        
    if (len(data) > 5):
        shear, normal, vert, hori = data.split(",")
        hori = hori.replace("\\r\\n", " ")
                
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
        if(cnt > 10):
            shearF.pop(0)
            normalF.pop(0)
            vertF.pop(0)
            horiF.pop(0)
            
            input("Aperte Enter para continuar: ")
        
    else:
        print("Aguardando entrada de dados!")       
