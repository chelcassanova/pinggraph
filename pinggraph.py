import os
import subprocess
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ping import Ping

ping = Ping()

fig = plt.figure()  # Create the main figure of the graph
fig.suptitle('AAAAAAAAAAAAAAAAAA')  # Give it a main title


ax = plt.subplot()  # Create an Axes object for the figure
ax.set_xlabel('wrgg')  # Set the label for the x-axis
ax.set_ylabel('Response Time (ms)')  # Set the label for the y-axis
plt.ion()

pingarray = []

def animate():
    pingarray.append(ping.call(1))
    plt.plot(pingarray)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
