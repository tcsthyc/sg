import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import gtreader as gtr


# functions
# def updateFig(data_total, data_index, data_middle, data_ring, data_little):
def updateFig(data_total):  
  line_total.set_ydata(data_total)
  # line_index.set_ydata(data_index)
  # line_middle.set_ydata(data_middle)
  # line_ring.set_ydata(data_ring)
  # line_little.set_ydata(data_little)
  # return line_total;

def data_gen():
  while True: yield np.random.rand(10)

# input meta info
# username = raw_input("plz enter username: ")

# init serial reader
gtr.init()
gtr.readData()


# init chart
fig = plt.figure(1)

ax_total = plt.subplot2grid((2,2),(0,0),colspan=2)
line_total, = ax_total.plot(np.random.rand(10))

ax_index = plt.subplot(245)
line_index, = ax_index.plot([4,5,6])

ax_middle = plt.subplot(246)
line_middle,  = ax_middle.plot([7,10,12])

ax_ring = plt.subplot(247)
line_ring, = ax_ring.plot([7,10,12])

ax_little = plt.subplot(248)
line_little, = ax_little.plot([7,10,12])

ani = animation.FuncAnimation(fig, updateFig, data_gen, interval=80)
plt.show()

# refresh chart
# def refreshChart():


# initChart()


