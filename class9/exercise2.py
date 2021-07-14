#!/usr/bin/env python

"""
2a. Create a new file named "my_functions.py" that will store a set of reusable functions. 
Move the "open_napalm_connection" function from exercise1 into this Python file. 
Import the network devices once again from my_devices.py and 
create a list of connection objects (once again with connections to both cisco3 and arista1).

2b. Pretty print the arp table for each of these devices. 
Gather this information using the appropriate NAPALM Getter.

2c. Attempt to use the get_ntp_peers() method against both of the devices. 
Does this method work? Your code should gracefully handle any exceptions that occur. 
In other words, an exception that occurs due to this get_ntp_peers() method, 
should not cause the program to crash.

2d. Create another function in "my_functions.py". 
This function should be named "create_backup" and should accept 
a NAPALM connection object as an argument. 
Using the NAPALM get_config() method, the function should retrieve and write 
the current running configuration to a file. 
The filename should be unique for each device. 
In other words, "cisco3" and "arista1" should each have a separate file 
that stores their running configuration. 
Note, get_config() returns a dictionary where the running-config is referenced 
using the "running" key. Call this function as part of your main exercise2 
and ensure that the configurations from both cisco3 and arista1 are backed up properly.
"""

import my_devices
from pprint import pprint
from napalm import get_network_driver
from my_functions import napalm_conn, create_backup

if __name__=="__main__":

    cisco3 = my_devices.cisco3
    arista1 = my_devices.arista1

    devices = list()
    devices.append(cisco3)
    devices.append(arista1)

    for device in devices:

        # Creating the napalm connection

        device_conn = napalm_conn(device)

        print("#" * 50)
        print(f"Printing {device['hostname']} napalm connection: ")
        print("#" * 50)
        print(device_conn)
    
        # Napalm get_arp_table getter

        arp_output = device_conn.get_arp_table()
        print("#" * 50)
        print(f"Printing {device['hostname']} arp table: ")
        print("#" * 50)
        pprint(arp_output)

        # Napalm get_ntp_peers getter

        try:
            ntp_output = device_conn.get_ntp_peers()

            print("#" * 50)
            print(f"Printing {device['hostname']} ntp peers: ")
            print("#" * 50)
            pprint(ntp_output)

        except NotImplementedError:

            print("#" * 50)
            print(f"{device['hostname']} does not support 'get_ntp_peers' getter")
            print("#" * 50)

        # Create and backing up running config

        running_conf = create_backup(device_conn)['running']

        print("#" * 50)
        print(f"Printing {device['hostname']} running config: ")
        print("#" * 50)

        pprint(running_conf)

        filename = f"{device['hostname']}_config"

        with open(filename, "w") as f:
            f.write(running_conf)

        device_conn.close()

