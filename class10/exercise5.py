#!/usr/bin/env python

""" 
5. Using a context manager and a 'ProcessPoolExecutor', 
complete the same task as Exercise 4.
"""

import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from my_devices import devices
from my_functions import ssh_command2

show_command = "show version"

def main():
    """
    Use ProcessPoolExecutor with 'as_completed' method and Netmiko to connect to each of the devices
    Execure 'show version' on each device
    Record the amount of time required to complete this
    """


    t0 = time.time()

    max_threads = 4

    # Use context manager to gracefully cleanup the pool
    with ProcessPoolExecutor(max_threads) as pool:

        future_list = []

        for device in devices:
            future = pool.submit(ssh_command2, device, show_command)
            future_list.append(future)

        for future in as_completed(future_list):
            print("#" * 80)
            print("OUTPUT: ")
            print(future.result())
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

