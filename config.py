port = 6
baudRate = 115200
timeout = 200
bytesize = 8
parity = 'N'
stopbits = 1
xonxoff = 0
rtscts = 0 


# unit: second, tested by delta_time_test.py
deltaTime = 0.00144471999884

# x axis refresh range
x_range = 10

# y axis range
y_min = 90
y_max = 1000

y_total_min = 360
y_total_max = 4000

bufferSize = int(x_range / deltaTime)
