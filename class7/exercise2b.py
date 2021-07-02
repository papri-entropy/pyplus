#!/usr/bin/env python

"""
2b. Print the names and an index number of each security zone in the XML data from Exercise 2a. 
Your output should look similar to the following (tip, enumerate will probably help):

Security Zone #1: trust
Security Zone #2: untrust
Security Zone #3: junos-host
"""


from pprint import pprint
import xmltodict

with open("show_security_zones.xml") as f:
    xml_str = f.read().strip()

xml_data = xmltodict.parse(xml_str)

print("#" * 50)
print("Printing var after parsing with xmltodict.parse")
print("#" * 50)

pprint(xml_data['zones-information']['zones-security'])

print(type(xml_data['zones-information']['zones-security']))

for count, zone in enumerate(xml_data['zones-information']['zones-security'], start=1):
    print(f"Security Zone #{count}: {zone['zones-security-zonename']}")



