import threading

class ReadDataThread (threading.Thread):
  def __init__(self, threadID, name, queue):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.data = queue

  def readData(self):
  	while True:
		print 'thread-read:'
		print self.data.get()

  def run(self):
    print "Start thread to read: " + self.name
    self.readData()    
    print "Exiting " + self.name


def init(queue):
	th = ReadDataThread(1, "Thread-2", queue)
	th.start()