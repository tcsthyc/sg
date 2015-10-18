import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import gtreader as gtr
import config as cfg

# functions
# def updateFig(data_total, data_index, data_middle, data_ring, data_little):
def updateFig(data):
  global ax_total,ax_index,ax_middle,ax_ring,ax_little
  # print 'update'
  # print len(gtr.recorder_total.records)

  if len(gtr.recorder_total.records) == 0:
    return
  else:
    x_start = (gtr.totalCount / cfg.bufferSize) * cfg.x_range
    x_end = x_start + cfg.x_range
    ax_total.set_xlim(x_start, x_end)
    ax_index.set_xlim(x_start, x_end)
    ax_middle.set_xlim(x_start, x_end)
    ax_ring.set_xlim(x_start, x_end)
    ax_little.set_xlim(x_start, x_end)
    x_arr = []

    rec_t = gtr.recorder_total.records[:]
    rec_i = gtr.recorder_index.records[:]
    rec_m = gtr.recorder_middle.records[:]
    rec_r = gtr.recorder_ring.records[:]
    rec_l = gtr.recorder_little.records[:]

    for i in range(len(rec_t)):
      x_arr.append(x_start + i*cfg.deltaTime)

    # print len(x_arr)
    # print len(rec_t)
    # print '----------------------------------'
    # print x_start
    # print gtr.totalCount
    # print cfg.x_range
    # print x_arr
    # print rec
    
    # print len(x_arr)
    # print len(rec)
    # print '------------------------------------'
    ax_total.scatter(x_arr,rec_t,0.6)
    ax_index.scatter(x_arr,rec_i,0.6)
    ax_middle.scatter(x_arr,rec_m,0.6)
    ax_ring.scatter(x_arr,rec_r,0.6)
    ax_little.scatter(x_arr,rec_l,0.6)
    return

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
ax_total.set_ylim(cfg.y_total_min,cfg.y_total_max)

ax_index = plt.subplot(245)
ax_index.set_xlim(0, cfg.x_range)
ax_index.set_ylim(cfg.y_min,cfg.y_max)

ax_middle = plt.subplot(246)
ax_middle.set_xlim(0, cfg.x_range)
ax_middle.set_ylim(cfg.y_min,cfg.y_max)

ax_ring = plt.subplot(247)
ax_ring.set_xlim(0, cfg.x_range)
ax_ring.set_ylim(cfg.y_min,cfg.y_max)

ax_little = plt.subplot(248)
ax_little.set_xlim(0, cfg.x_range)
ax_little.set_ylim(cfg.y_min,cfg.y_max)

ax_start = plt.axes([0.02,0.92,0.08,0.05])


btn_start = Button(ax_start, 'start')
btn_start.on_clicked(startPort)

ani = animation.FuncAnimation(fig, updateFig, data_gen, interval=30)
plt.show()