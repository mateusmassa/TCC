import signal
from time import sleep

def handler(signum, frame):
    print 'Funcao secundaria'
    signal.alarm(5)

# Set the signal handler and a 5-second alarm
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

print 'Funcao principal'

signal.pause();


#signal.alarm(0)          # Disable the alarm