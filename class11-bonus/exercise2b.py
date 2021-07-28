#!/usr/bin/env python

"""
2a. Using the Python requests library, perform an HTTP GET on the base URL of the NetBox server 
(https://netbox.lasthop.io/api/). Ensure that you are not verifying the SSL certificate. 
Print the HTTP status code, the response text, the JSON response, and the HTTP response headers. 
These items can be accessed using the following attributes/methods in the Python-requests Response object:

response.status_code
response.text
response.json()
response.headers
"""

import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

if __name__=="__main__":

    url = "https://netbox.lasthop.io/api/"

    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    
    response = requests.get(url, headers=http_headers, verify=False)

    print("#" * 80)
    print("Printing the HTTP status code: ")
    print("#" * 80)
    print(response.status_code)

    print("#" * 80)
    print("Printing the response text: ")
    print("#" * 80)
    print(response.text)

    print("#" * 80)
    print("Printing the JSON response: ")
    print("#" * 80)
    print(response.json())

    print("#" * 80)
    print("Printing the HTTP response headers: ")
    print("#" * 80)
    print(response.headers)
