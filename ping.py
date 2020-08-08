import subprocess
import re
import sys
import threading

class Ping:
    """A class that will get the response from the ping call"""

    def __init__(self):
        response = 0

    def call(self, ostype, server="google.com"):
        """
        A function that makes a call to the system's 'ping' command and returns the numerical response time
        """
        pingvalue = 0
        
        # Gathering ping data
        # If ostype is 0, then it's the Windows version of the command
        # If ostype is 1, then it uses the Bash command
        # TODO: Threading might make this part run better (as in, not stall whenever the connection is bad)
        if ostype == 0:
            command = str.format("ping -n 1 {}", server)
        else:
            command = str.format("ping -c 1 {}", server)

        # This block will get the full response of the call to the ping command as a byte string
        # The try-except block catches when the ping call doesn't give a response (the connection drops)
        # In that case it returns 0
        # Again, there's a better way to do this (catch when the exit status is non-zero instead of a try-except)

        try:
            pingresponse = subprocess.check_output(command, shell=True)
        except subprocess.CalledProcessError:
            return 0

        # The entire byte string is then split into its individual words
        pinglist = pingresponse.split(b'\n')

        for line in pinglist:
            line = line.decode("utf-8")  # Decode the byte strings into normal unicode lines

            # Allows us to only care about lines that have the actual ping value
            if "time=" in line:
                # Spilt the line by the "time=" and "ms".
                # This gives us a list where the second index is the ping value itself
                # I'm sure there's a better way to do it though
                pingline = re.split(r'time=|ms', line)
                pingvalue = float(pingline[1])  # Converted to a float rather than an int for the Bash command
                
        return pingvalue


def main():
    ping = Ping()
    ostype = int(sys.argv[1])
    while True:
        print(ping.call(ostype))


if __name__ == '__main__':
    main()



