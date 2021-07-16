#!/usr/bin/env python

"""
4a. Add nxos1 to your my_devices.py file. 
Ensure that you include the necessary information to set the NX-API port to 8443. 
This is done using 'optional_args' in NAPALM so you should have the following key-value pair defined:

"optional_args": {"port": 8443}

4b. Create a new function named 'create_checkpoint'. 
Add this function into your my_functions.py file. 
This function should take one argument, the NAPALM connection object. 
This function should use the NAPALM _get_checkpoint_file() method 
to retrieve a checkpoint from the NX-OS device. 
It should then write this checkpoint out to a file.

Recall that the NX-OS platform requires a 'checkpoint' file 
for configuration replace operations. 
Using this new function, retrieve a checkpoint 
from nxos1 and write it to the local file system.

4c. Manually copy the saved checkpoint to a new file 
and add an additional loopback interface to the configuration.

4d. Create a Python script that stages a complete configuration replace operation 
(using the checkpoint file that you just retrieved and modified). 
Once your candidate configuration is staged perform a compare_config (diff) 
on the configuration to see your pending changes. 
After the compare_config is complete, then use the discard_config() method 
to eliminate the pending changes. 
Next, perform an additional compare_config (diff) to verify that you have 
no pending configuration changes. 
Do not actually perform the commit_config as part of this exercise.
"""

import my_devices
from pprint import pprint
from napalm import get_network_driver
from my_functions import napalm_conn, create_backup, create_checkpoint

if __name__=="__main__":

    # Creating the nxos napalm connection

    nxos1 = my_devices.nxos1
    nxos1_hostname = nxos1['hostname']

    device_conn = napalm_conn(nxos1)

    print("#" * 50)
    print(f"Printing {nxos1_hostname} napalm connection: ")
    print("#" * 50)

    print(device_conn)

    # Creating the nxos checkpoint file

    filename = f"{nxos1_hostname}_checkpoint" 

    checkpoint = create_checkpoint(device_conn, filename) 
    
    # Napalm Config Replace staging 
    
    device_conn.load_replace_candidate(filename=f"{nxos1_hostname}_config")

    print("#" * 50)
    print(f"Printing {nxos1_hostname} DIFFS candidate vs running before commiting: ")
    print("#" * 50)
    print(device_conn.compare_config()) 

    device_conn.discard_config()

    print("#" * 50)
    print(f"Printing {nxos1_hostname} DIFFS candidate vs running after discarding the staged candidate: ")
    print("#" * 50)
    print(device_conn.compare_config()) 
    
    device_conn.close()    


