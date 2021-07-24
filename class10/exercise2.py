#!/usr/bin/env python

"""
2. Create a new file named my_functions.py. 
Move your function from exercise1 to this file. 
Name this function "ssh_command". 
Reuse functions from this file for the rest of the exercises. 
Complete the same task as Exercise 1b except this time use 
"legacy" threads to create a solution. Launch a separate thread 
for each device's SSH connection. 
Print the time required to complete the task for all of the devices. 
Move all of the device specific output printing 
to the called function (i.e. to the child thread). 
"""

import threading
import time
from my_functions import ssh_command
from my_devices import devices


show_command = "show version"

def main(): 
    """
    Use threads and Netmiko to connect to each of the devices
    Execure 'show version' on each device.
    Record the amount of time required to complete this
    """

    t0 = time.time()

    for device in devices:
        my_thread = threading.Thread(target=ssh_command, args=(device, show_command))
        my_thread.start()

    main_thread = threading.currentThread()
    print(threading.enumerate())
    for some_thread in threading.enumerate():
        if some_thread != main_thread:
            print(some_thread)
            some_thread.join()

    print("#" * 80)
    print(f"Execution time: {time.time() - t0:.2f} seconds")
    print("#" * 80)


if __name__=="__main__":
    main()

