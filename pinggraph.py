import os
import subprocess
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
from ping import Ping

ping = Ping()

fig = plt.figure()  # Create the main figure of the graph
fig.suptitle('AAAAAAAAAAAAAAAAAA')  # Give it a main title


ax = plt.subplot()  # Create an Axes object for the figure
ax.set_xlabel('wrgg')  # Set the label for the x-axis
ax.set_ylabel('Response Time (ms)')  # Set the label for the y-axis
# plt.ion()

pingarray = []

# PROBLEM: Cross-platform program only works on Windows
# TODO: Get graph to be one colour
def animate(i, ostype=0):  # I don't know why, but the func def needs an argument
    pingresponse = ping.call(ostype)  # Get the response time of the ping call
    pingarray.append(pingresponse)  # Add that response time to a list of responses for plotting
    plt.plot(pingarray)  # Plot the current array

    # If there are more than 20 items in the array
    # then clear the current axes, remove the very first item
    # and plot again. This is what makes the graph look like it's "scrolling"
    if len(pingarray) > 20:
        plt.cla()
        pingarray.pop(0)
        plt.plot(pingarray)

    # Update the y-axis label with the current ping value
    ax.set_ylabel(str.format('Response Time (ms): {}', pingresponse))


def main():
    # If this is being run on Windows, set the "os type" to 0, otherwise, set it to 1
    if sys.platform == "win32":
        osint = 0
    else:
        osint = 1
    ani = animation.FuncAnimation(fig, animate, fargs=(osint), interval=500)
    plt.show()


if __name__ == '__main__':
    main()
