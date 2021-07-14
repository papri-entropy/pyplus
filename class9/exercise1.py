#!/usr/bin/env python

"""
1a. Create a Python file named "my_devices.py" that defines the NAPALM connection information 
for both the 'cisco3' device and the 'arista1' device. Use getpass() for the password handling. 
This Python module should be used to store the device connection information 
for all of the exercises in this lesson.

1b. Create a simple function that accepts the NAPALM device information from the my_devices.py file 
and creates a NAPALM connection object. 
This function should open the NAPALM connection to the device and should return the NAPALM connection object.

1c. Using your "my_devices.py" file and your NAPALM connection function, 
create a list of NAPALM connection objects to 'cisco3' and 'arista1'.

1d. Iterate through the connection objects, print out the device's connection object itself. 
Additionally, pretty print the facts for each device 
and also print out the device's NAPALM platform type (ios, eos, et cetera).
"""

import my_devices
from pprint import pprint
from napalm import get_network_driver

# Creating napalm connection function

def napalm_conn(device):

    device_type = device.pop("device_type")
    driver = get_network_driver(device_type)
    device_conn = driver(**device)
    device_conn.open()
    
    return device_conn

if __name__=="__main__":

    cisco3 = my_devices.cisco3
    arista1 = my_devices.arista1

    devices = list()
    devices.append(cisco3)
    devices.append(arista1)

    for device in devices:

        device_conn = napalm_conn(device)

        print("#" * 50)
        print(f"Printing {device['hostname']} napalm connection: ")
        print("#" * 50)
        print(device_conn)

        facts_output = device_conn.get_facts()

        print("#" * 50)
        print(f"Printing {device['hostname']} facts: ")
        print("#" * 50)
        pprint(facts_output)

        platform_output = device_conn.platform

        print("#" * 50)
        print(f"Printing {device['hostname']} platform: ")
        print("#" * 50)
        print(platform_output)

        device_conn.close()


