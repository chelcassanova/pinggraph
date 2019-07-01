import subprocess
import re

try:
    import simplejson as json
except ImportError:
    import json

class Ping:
    """A class that will get the response from the ping call"""

    def __init__(self):
        response = 0

    def call(self):
        """
        The function that gets the response itself
        """
        pingvalue = 0

        # Gathering ping data
        command = "ping -n 1 google.com"

        """
        This try-except block catches when the ping call doesn't give a response (the connection drops)
        In that case it returns 0 
        Again, there's a better way to do this (catch when the exit status is non-zero instead of a try-except)
        """
        try:
            pingresponse = subprocess.check_output(command, shell=True)
        except subprocess.CalledProcessError:
            return 0

        pinglist = pingresponse.split(b'\n')


        for line in pinglist:
            line = line.decode("utf-8")  # Decode the byte strings into normal unicode lines

            # Allows us to only care about lines that have the actual ping value
            if "time=" in line:
                # FUCK YES
                """
                Spilt the line by the "time=" and "ms". 
                This gives us a list where the second index is the ping value itself
                I'm sure there's a better way to do it though
                """
                pingline = re.split(r'time=|ms', line)
                pingvalue = int(pingline[1])
                # json.dump(pingline[1])
        return pingvalue

def main():
    ping = Ping()
    while True:
        print(ping.call())

if __name__ == '__main__':
    main()



