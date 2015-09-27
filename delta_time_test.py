import serial
import config as cfg
import time

total = 20000

ser = serial.Serial()
ser.baudrate = cfg.baudRate
ser.port = cfg.port
ser.timeout = cfg.timeout
ser.bytesize = cfg.bytesize
ser.parity = cfg.parity
ser.stopbits = cfg.stopbits
ser.xonxoff = cfg.xonxoff
ser.rtscts = cfg.rtscts
ser = ser
ser.open()

started = False
count = 0

while not started:
  line = ser.readline()
  started = 'Start' in line

startTime = time.time()
while count < total:
  line = ser.readline()
  count = count + 1 
  print count
deltaTime = time.time() - startTime

print deltaTime/total

ser.close()

