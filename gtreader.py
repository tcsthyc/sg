import serial
import config as cfg
import thread
import threading
import time

class Recorder:
  def __init__(self,bufferSize):
    self.records = []
    self.bufferSize = bufferSize
    self.pos = 0
  def record(self,data):
    if len(self.records) < self.bufferSize:
      self.records.append(data)
      self.pos += 1
    else:
      self.pos %= self.bufferSize
      self.records[self.pos] = data
      self.pos += 1

dataCache = []
totalCount = 0
recorder_total = Recorder(cfg.bufferSize)
recorder_index = Recorder(cfg.bufferSize)
recorder_middle = Recorder(cfg.bufferSize)
recorder_ring = Recorder(cfg.bufferSize)
recorder_little = Recorder(cfg.bufferSize)

class ReadThread (threading.Thread):
  def __init__(self, threadID, name, counter):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.started = False
    self.initSer()

  def initSer(self):
    ser = serial.Serial()
    ser.baudrate = cfg.baudRate
    ser.port = cfg.port
    ser.timeout = cfg.timeout
    ser.bytesize = cfg.bytesize
    ser.parity = cfg.parity
    ser.stopbits = cfg.stopbits
    ser.xonxoff = cfg.xonxoff
    ser.rtscts = cfg.rtscts
    self.ser = ser

  def readData(self):
    global dataCache, totalCount, recorder_total, recorder_index, recorder_middle, recorder_ring, recorder_little
    self.ser.open()
    while not self.started:
      line = self.ser.readline()
      self.started = 'Start' in line
    while True:
      line = self.ser.readline()
      print line
      words = line.split(' ')
      print words
      values = map(lambda x:float(x),words)
      dataCache.append(values)
      totalCount = totalCount + 1
      recorder_total.record(values[0]+values[1]+values[2]+values[3])
      recorder_index.record(values[0])
      recorder_middle.record(values[1])
      recorder_ring.record(values[2])
      recorder_little.record(values[3])

  def run(self):
    print "Start thread to read: " + self.name
    self.readData()    
    print "Exiting " + self.name

  def stop(self):
    self.ser.close()


def init():
  th = ReadThread(1, "Thread-1", 10)
  th.start()
