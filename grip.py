import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import gtreader as gtr
from matplotlib.widgets import Button
import config as cfg

# functions
# def updateFig(data_total, data_index, data_middle, data_ring, data_little):
def updateFig(data):
  if len(gtr.recorder_total.records) == 0:
    return
  # else:
  #   x_start = (gtr.totalCount / cfg.bufferSize) * cfg.x_range
  #   x_end = x_start + cfg.x_range
  #   ax_total.set_xlim(x_start, x_end)
  #   ax_index.set_xlim(x_start, x_end)
  #   ax_middle.set_xlim(x_start, x_end)
  #   ax_ring.set_xlim(x_start, x_end)
  #   ax_little.set_xlim(x_start, x_end)
  #   x_arr = []
  #   for i in range(len(gtr.recorder_total.records)):
  #     x_arr.append(x_start + i*cfg.deltaTime)
  #   print len(x_arr)
  #   print len(gtr.recorder_total.records)
  #   ax_total.scatter(x_arr,gtr.recorder_total.records)
  #   ax_index.scatter(x_arr,gtr.recorder_index.records)
  #   ax_middle.scatter(x_arr,gtr.recorder_middle.records)
  #   ax_ring.scatter(x_arr,gtr.recorder_ring.records)
  #   ax_little.scatter(x_arr,gtr.recorder_little.records)

def data_gen():
  yield []

def startPort(event):
  gtr.init()

# input meta info
# username = raw_input("plz enter username: ")

# init chart
fig = plt.figure(1)

ax_total = plt.subplot2grid((2,2),(0,0),colspan=2)
ax_total.set_xlim(0, cfg.x_range)
ax_total.set_ylim(cfg.y_min,cfg.y_max)
# ax_total.scatter(range(10),range(10))

ax_index = plt.subplot(245)
ax_index.set_xlim(0, cfg.x_range)
ax_index.set_ylim(cfg.y_min,cfg.y_max)
# ax_index.scatter(range(10),range(10))

ax_middle = plt.subplot(246)
ax_middle.set_xlim(0, cfg.x_range)
ax_middle.set_ylim(cfg.y_min,cfg.y_max)
# ax_middle.scatter(range(10),range(10))

ax_ring = plt.subplot(247)
ax_ring.set_xlim(0, cfg.x_range)
ax_ring.set_ylim(cfg.y_min,cfg.y_max)
# ax_ring.scatter(range(10),range(10))

ax_little = plt.subplot(248)
ax_little.set_xlim(0, cfg.x_range)
ax_little.set_ylim(cfg.y_min,cfg.y_max)
# ax_little.scatter(range(10),range(10))

ax_start = plt.axes([0.02,0.92,0.08,0.05])
btn_start = Button(ax_start, 'start')
btn_start.on_clicked(startPort)

ani = animation.FuncAnimation(fig, updateFig, data_gen, interval=80)
plt.show()

