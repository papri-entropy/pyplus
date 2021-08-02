#!/usr/bin/env python

"""
2c. Execute another HTTP GET request to retrieve all of the endpoints under the "/api/dcim" parent. 
Pretty print out the response.json() from this output. 
This should be a dictionary with the key being the next part of the URL after "/api/dcim" 
and the value being the full URL.
"""

import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__=="__main__":

    url = "https://netbox.lasthop.io/api/dcim"

    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    
    response = requests.get(url, headers=http_headers, verify=False)

    print("#" * 80)
    print("Printing the JSON response: ")
    print("#" * 80)
    pprint(response.json())

