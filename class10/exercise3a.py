#!/usr/bin/env python

"""
3a. Create a new function that is a duplicate of your "ssh_command" function. 
Name this function "ssh_command2". This function should eliminate 
all printing to standard output and should instead return the show command output. 
Note, in general, it is problematic to print in the child thread as you can get 
into race conditions between the threads. 
Using the "ThreadPoolExecutor" in Concurrent Futures execute "show version" 
on each of the devices defined in my_devices.py. 
Use the 'wait' method to ensure all of the futures have completed. 
Concurrent futures should be executing the ssh_command2 function in the child threads. 
Print the total execution time required to accomplish this task.
"""

import time
from concurrent.futures import ThreadPoolExecutor, wait
from my_devices import devices
from my_functions import ssh_command2

show_command = "show version"

def main():
    """
    Use ThreadPoolExecutor with 'wait' method and Netmiko to connect to each of the devices
    Execure 'show version' on each device
    Record the amount of time required to complete this
    """

    
    t0 = time.time()

    max_threads = 4
    
    pool = ThreadPoolExecutor(max_threads)

    future_list = []
    for device in devices:
        future = pool.submit(ssh_command2, device, show_command)
        future_list.append(future)

    # Waits until all the pending threads are done

    wait(future_list)

    for future in future_list:
        print("#" * 80)
        print("OUTPUT: ")
        print(future.result())
        print("#" * 80)

    
    t1 = time.time()
    
    print("#" * 80)
    print(f"Execution time: {time.time() - t0:.2f} seconds")
    print("#" * 80)


if __name__=="__main__":
    main()



