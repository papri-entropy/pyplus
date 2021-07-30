#!/usr/bin/env python

"""
5. Building on the script from exercise 4, add a description to the the IP address object that you just created. 
Accomplish this using an HTTP PUT. The HTTP PUT operation will require all of the mandatory fields in the object 
(in this case, the "address" field). Print the status code and the response.json() from your PUT operation. 
The HTTP PUT operation will use same URL as exercise 4b (i.e. the URL of the newly created IP address object including its ID).
"""

import os
import json
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__=="__main__":

    ip_addr_url = "https://netbox.lasthop.io/api/ipam/ip-addresses/386/"

    # Set the token based on the NETBOX_TOKEN environment variable
    token = os.environ["NETBOX_TOKEN"]

    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    response = requests.get(ip_addr_url, headers=http_headers, verify=False)
    ip_id_386 = response.json()

    pprint(ip_id_386)

    # HTTP PUT Operation

    put_data = dict()
    
    put_data["address"] = ip_id_386["address"]
    put_data["description"] = "SWITCH-A" 

    put_response = requests.put(
        ip_addr_url, headers=http_headers, data=json.dumps(put_data), verify=False
    )

    print("#" * 80)
    print("Printing the HTTP status code: ")
    print("#" * 80)
    print(put_response.status_code)

    print("#" * 80)
    print("Printing HTTP PUT to modify an IP address object: ")
    print("#" * 80)
    put_response = put_response.json()
    print()
    pprint(put_response)
    print()




