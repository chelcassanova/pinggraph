import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
from ping import Ping

ping = Ping()

fig = plt.figure()  # Create the main figure of the graph
fig.suptitle('Ping Response Graph')  # Give it a main title
fig.canvas.toolbar.pack_forget()  # Remove toolbar
fig.canvas.set_window_title('Ping Graph')


ax = plt.subplot()  # Create an Axes object for the figure
ax.set_xlabel('Time?')  # Set the label for the x-axis
ax.set_ylabel('Response Time (ms)')  # Set the label for the y-axis

pingarray = []


def animate(i, ostype, server):  # I don't know why, but the func def needs an argument
    pingresponse = ping.call(ostype, server)  # Get the response time of the ping call
    pingarray.append(pingresponse)  # Add that response time to a list of responses for plotting

    if pingresponse == 0:
        plt.plot(pingarray, 'r')  # Plot the current array
    else:
        plt.plot(pingarray, 'b')  # Plot the current array

    # If there are more than 20 items in the array
    # then clear the current axes, remove the very first item
    # and plot again. This is what makes the graph look like it's "scrolling"
    if len(pingarray) > 20:
        plt.cla()
        pingarray.pop(0)
        if pingresponse == 0:
            plt.plot(pingarray, 'r')  # Plot the current array (in red)
        else:
            plt.plot(pingarray, 'b')  # Plot the current array

    # Update the y-axis label with the current ping value
    ax.set_xlabel('Time')
    ax.set_ylabel(str.format('Response Time (ms): {}', pingresponse))
    fig.suptitle(str.format('Pinging {}', server))


def main():
    # If this is being run on Windows, set the "os type" to 0, otherwise, set it to 1
    if sys.platform == "win32":
        osint = 0
    else:
        osint = 1

    # All it took was putting a comma after 'osint' in fargs >:(
    # TODO: Make the "what server do you want to ping" a GUI thing
    # TODO: Create a .exe from this
    pingserver = input("Type a web address or an IP address to ping")
    ani = animation.FuncAnimation(fig, animate, 25, fargs=(osint, pingserver), interval=150)
    plt.show()



if __name__ == '__main__':
    main()
