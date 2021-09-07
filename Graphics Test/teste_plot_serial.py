# -*- coding: utf-8 -*-
import serial                          # carrega a biblioteca serial
from time import sleep                 # carrega a biblioteca time
import numpy                           # carrega a biblioteca numpy
import matplotlib.pyplot as plt        # carrega a biblioteca pyplot
import matplotlib.gridspec as gridspec # carrega a biblioteca gridspec
from drawnow import *                  # carrega a biblioteca drawnow
from array import array                # carrega a biblioteca array
import os


loadF = array('f') 

# ----- Setup the Serial COM Port ------
arduinoData = serial.Serial(
port='/dev/ttyUSB0',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)

plt.ion()

cnt = 0

#function makeFig()
def makeFig():
    gs = gridspec.GridSpec(3, 3)
    #Plot 1
    plt.subplot(gs[0, :])
    plt.ylim([0,40])
    plt.title('Shear Load')
    plt.grid(True)
    plt.ylabel('Load')
    plt.xlabel('Medida')
    plt.plot(loadF, 'ro-', label='Shear Load [N]')
    plt.legend(loc='upper left')
    

# ----- Read the Shear Load -----

while 1:
    
    arduinoData.write('*1B1\n')
    data = arduinoData.readline()
    data = data[:-1]
    
    if (len(data) != 0):
        dataF = float(data.strip().replace(",", "."))
    else:
        dataF = 0.00;
        
    loadF.append(dataF)
    drawnow(makeFig)
    plt.pause(.000005)
    cnt = cnt + 1
    if(cnt > 20):
        loadF.pop(0)
        raw_input("Aperte Enter para continuar: ")
        
    
        
