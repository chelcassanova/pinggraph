import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
import tkinter
from ping import Ping


ping = Ping()  # Create a new ping object

fig = plt.figure()  # Create the main figure of the graph
ax = plt.subplot()  # Create an Axes object for the figure
ax.set_xlabel('Time?')  # Set the label for the x-axis
ax.set_ylabel('Response Time (ms)')  # Set the label for the y-axis

pingarray = []  # Create a list that will be used to hold the ping response times


def animate(i, ostype, server):  # NOTE: I don't know why, but the func def needs an argument
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
            plt.plot(pingarray, 'r')  # Plot the current array
        else:
            plt.plot(pingarray, 'b')  # Plot the current array

    # Update the y-axis label with the current ping value
    ax.set_xlabel('Time?')
    ax.set_ylabel(str.format('Response Time (ms): {}', pingresponse))
    fig.suptitle(str.format('Pinging {}', server))


def serverwindow():
    """
    A graphical window that can be used to enter the server to ping instead of using the command line
    :return: The server that the user want to ping
    """
    window = tkinter.Tk()
    window.geometry("300x150")
    messagelabel = tkinter.Label(window, text="Please enter the server you want to ping")
    messagelabel.pack()

    entrystring = "google.com"
    serverentry = tkinter.Entry(window, text="pls")
    serverentry.pack()
    serverentry.insert(0, entrystring)

    """
    PROBLEM: This might not be possible because of the way I set it up (putting it inside a function)
    and the fact that Tkinter is event driven (callback functions shouldn't return anything)
    """
    # window.bind("<Return>", returnserver)
    window.mainloop()


def main():
    # If this is being run on Windows, set the "os type" to 0, otherwise, set it to 1
    if sys.platform == "win32":
        osint = 0
    else:
        osint = 1

    # All it took was putting a comma after 'osint' in fargs >:(
    # TODO: Make the "what server do you want to ping" a GUI thing
    pingserver = "google.com"
    serverwindow()
    ani = animation.FuncAnimation(fig, animate, 25, fargs=(osint, pingserver), interval=200)
    plt.show()


if __name__ == '__main__':
    main()
