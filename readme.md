This is a program that calls the terminal-based ping command, gets the ms value of the ping, and converts the value into a graph.

Basically, it turns this:

![alt text][pingterm]

into this:

![alt text][pinggraph]


[pingterm]: images/pingterm.png "The ping command running in Windows Powershell"
[pinggraph]: images/pinggraph.png "The Ping Graph program running"

This program is run via command-line by typing `python3 pinggraph.py`. The user is then prompted to enter a web address or IP address to ping.

This program works on Windows and Linux-based OSes such as Ubuntu.
