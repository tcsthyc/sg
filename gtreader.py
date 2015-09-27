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
recorder_total = Recorder(cfg.bufferSize)
recorder_index = Recorder(cfg.bufferSize)
recorder_middle = Recorder(cfg.bufferSize)
recorder_ring = Recorder(cfg.bufferSize)
recorder_little = Recorder(cfg.bufferSize)

class ReadThread (threading.Thread):
  def __init__(self, threadID, name, counter):
    threading.Thread.__init__(self)
    self.threadID = threadID
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
    ser.open()
    self.ser = ser

  def run(self):
    print "Starting " + self.name
    print_time(self.name, self.counter, 0.5)
    print "Exiting " + self.name

def print_time(threadName, counter, delay):
  while counter:
    time.sleep(delay)
    print "%s: %s" % (threadName, time.ctime(time.time()))
    counter -= 1


def init():
  global ser
  ser = serial.Serial()
  ser.baudrate = cfg.baudRate
  ser.port = cfg.port
  ser.timeout = cfg.timeout
  ser.bytesize = cfg.bytesize
  ser.parity = cfg.parity
  ser.stopbits = cfg.stopbits
  ser.xonxoff = cfg.xonxoff
  ser.rtscts = cfg.rtscts
  ser.open()
  
  # th = ReadThread(1, "Thread-1", 10)
  # th.start()

def readData():
  global ser, dataCache, recorder_total, recorder_index, recorder_middle, recorder_ring, recorder_little
  while True:
    line = ser.readline()
    # line = '1 2 3 4 10'
    words = line.split(' ')
    values = map(lambda x:float(x),words)
    dataCache.append(values)
    print dataCache
    recorder_total.record(values[0]+value[1]+value[2]+value[3])
    recorder_index.record(values[0])
    recorder_middle.record(values[1])
    recorder_ring.record(values[2])
    recorder_little.record(values[3])

def end():
  global ser
  ser.close()
