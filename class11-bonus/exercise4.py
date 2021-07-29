#!/usr/bin/env python

"""
4a. Using an HTTP POST and the Python-requests library, create a new IP address in NetBox. 
This IP address object should be a /32 from the 192.0.2.0/24 documentation block. 
Print out the status code and the returned JSON.

The HTTP headers for this request should look as follows:

http_headers = {}
http_headers["Content-Type"] = "application/json; version=2.4;"
http_headers["accept"] = "application/json; version=2.4;"
http_headers["Authorization"] = f"Token {token}"

The URL for the HTTP POST is:

https://netbox.lasthop.io/api/ipam/ip-addresses/

The JSON payload data for this request should be similar to the following:

data = {"address": "192.0.2.100/32"}

4b. Using the response data from the HTTP POST that created the IP address entry in exercise 4a, 
capture the "id" of the newly created IP address object. Using this ID, construct a new URL. 
Use this new URL and the HTTP GET method to retrieve only the API information specific to this IP address. 
Your IP address URL should be of the following form:

https://netbox.lasthop.io/api/ipam/ip-addresses/{address_id}/

where {address_id} is the ID of the object that you just created.

Pretty print the response.json() data from this HTTP GET. Please note the ID of the address object that you just created.
"""

import os
import json
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__=="__main__":

    ip_addr_url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"

    # Set the token based on the NETBOX_TOKEN environment variable
    token = os.environ["NETBOX_TOKEN"]

    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    post_data = {"address": "192.0.2.44/32"}
    
    post_response = requests.post(
        ip_addr_url, headers=http_headers, data=json.dumps(post_data), verify=False
    )

    print("#" * 80)
    print("Printing the HTTP status code: ")
    print("#" * 80)
    print(post_response.status_code)

    print("#" * 80)
    print("Printing HTTP POST to create the new IP address: ")
    print("#" * 80)
    post_response = post_response.json()
    pprint(post_response)


    new_ip_obj_id = post_response['id']
    print("#" * 80)
    print("Printing the new IP address object ID: ")
    print("#" * 80)
    print(new_ip_obj_id) 

    new_ip_url = f"{ip_addr_url}{new_ip_obj_id}/"

    get_response = requests.get(
        new_ip_url, headers=http_headers, verify=False
    )

    print("#" * 80)
    print("Printing HTTP GET API information new IP: ")
    print("#" * 80)
    pprint(get_response.json()) 
    


