#!/usr/bin/env python

""" 
6. Using a context manager, the ProcessPoolExecutor, and the map() method, 
create a solution that executes "show ip arp" on all of the devices defined in my_devices.py. 
Note, the Juniper device will require "show arp" instead of "show ip arp" 
so your solution will have to properly account for this.
"""

import time
from concurrent.futures import ProcessPoolExecutor
from my_devices import devices
from my_functions import ssh_command3


def main():
    """
    Use ProcessPoolExecutor with 'map' method and Netmiko to connect to each of the devices
    Execure 'show version' on each device
    Record the amount of time required to complete this
    """


    t0 = time.time()

    max_threads = 4

    # Use context manager to gracefully cleanup the pool
    with ProcessPoolExecutor(max_threads) as pool:
        results_generator = pool.map(ssh_command3, devices)

        # Results generator
        for result in results_generator:
            

            print("#" * 80)
            print("OUTPUT: ")
            print(result)
            print("#" * 80)

            t1 = time.time()

            # Print individual device execution time

            print("#" * 80)
            print(f"Execution time: {t1 - t0:.2f} seconds")
            print("#" * 80)


        print("#" * 80)
        print(f"TOTAL Execution time: {time.time() - t0:.2f} seconds")
        print("#" * 80)

if __name__=="__main__":
    main()

