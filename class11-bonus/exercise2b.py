#!/usr/bin/env python

"""
2b. Repeat exercise 2a, except properly construct the HTTP request headers as follows:

http_headers = {}
http_headers["accept"] = "application/json; version=2.4;"

You will need to pass these HTTP headers into your HTTP GET request. 
Once again print the HTTP status code, the response text, the JSON response, and the HTTP response headers. 
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
