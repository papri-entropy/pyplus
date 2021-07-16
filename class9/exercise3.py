#!/usr/bin/env python

"""
3a. Using your existing functions and the my_devices.py file, 
create a NAPALM connection to both cisco3 and arista1.

3b. Create two new text files `arista1.lasthop.io-loopbacks` and `cisco3.lasthop.io-loopbacks`. 
In each of these files, create two new loopback interfaces with a description. 
Your files should be similar to the following:

interface loopback100
  description loopback100
!
interface loopback101
  description loopback101

For both cisco3 and arista1, use the load_merge_candidate() method 
to stage the candidate configuration. In other words, use load_merge_candidate() 
and your loopback configuration file to stage a configuration change. 
Use the NAPALM compare_config() method to print out 
the pending differences (i.e. the differences between the running configuration and the candidate configuration).

3c. Commit the pending changes to each device, and check the diff once again (after the commit_config).
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
    
        # Load config change (merge) - no commit
        
        filename = f"{device['hostname']}-loopbacks" 
        device_conn.load_merge_candidate(filename=filename)

        print("#" * 50)
        print(f"Printing {device['hostname']} DIFFS Candidate vs Running: ")
        print("#" * 50)
        print(device_conn.compare_config())
        
        # Commiting the pending changes

        device_conn.commit_config()

        print("#" * 50)
        print(f"Printing {device['hostname']} DIFFS after Commit operation: ")
        print("#" * 50)
        print(device_conn.compare_config())
        
        device_conn.close() 
