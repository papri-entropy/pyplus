#!/usr/bin/env python

"""
6. Use an HTTP DELETE and Python-requests to delete the IP address object 
that you just created. Remember to reference the ID of your object.
"""

import os
import json
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__=="__main__":

    ip_addr_url = "https://netbox.lasthop.io/api/ipam/ip-addresses/389/"

    # Set the token based on the NETBOX_TOKEN environment variable
    token = os.environ["NETBOX_TOKEN"]

    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    # HTTP Delete IP address with object ID 389
    response = requests.delete(ip_addr_url, headers=http_headers, verify=False)

    if response.ok:
        print("IP address deleted successfully")
    else:
        print("Error occured")

    print("#" * 80)
    print("Printing the HTTP status code: ")
    print("#" * 80)
    print(response.status_code)




