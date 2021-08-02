#!/usr/bin/env python

"""
3b. Using the same device information retrieved in exercise 3a, 
create and print a report to standard output. 
This report should contain the location, manufacturer, and status for each device. 
Your output should look similar to the following:

------------------------------------------------------------
arista1
----------
Location: Fremont Data Center
Vendor: Arista
Status: Active
------------------------------------------------------------


------------------------------------------------------------
arista2
----------
Location: Fremont Data Center
Vendor: Arista
Status: Active
------------------------------------------------------------

...   # remaining devices
"""

import os
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__=="__main__":

    url = "https://netbox.lasthop.io/api/dcim/devices"

    # Set the token based on the NETBOX_TOKEN environment variable
    token = os.environ["NETBOX_TOKEN"]

    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    response = requests.get(url, headers=http_headers, verify=False)

    print("#" * 80)
    print("Printing a report of netbox devices inventory: ")
    print("#" * 80)

    response = response.json()['results']

    for device in response:
        print("-" * 80)
        print(device['display_name'])
        print("-" * 15)
        print(f"Location: {device['site']['name']}")
        print(f"Vendor: {device['device_type']['manufacturer']['name']}")
        print(f"Status: {device['status']['label']}")


    

