#!/usr/bin/env python

"""
3a. Open the following two XML files: show_security_zones.xml and show_security_zones_single_trust.xml. 
Use a generic function that accepts an argument "filename" to open and read a file. 
Inside this function, use xmltodict to parse the contents of the file. 
Your function should return the xmltodict data structure. 
Using this function, create two variables to store the xmltodict data structure from the two files.
"""

from pprint import pprint
import xmltodict

def xml_read(filename):
    with open(filename) as f:
        xml_str = f.read().strip()
    xml_data = xmltodict.parse(xml_str)
    return xml_data

sec_zones = xml_read("show_security_zones.xml")
sec_zones_trust = xml_read("show_security_zones_trust.xml")


print("#" * 50)
pprint(sec_zones)
print("#" * 50)
pprint(sec_zones_trust)
print("#" * 50)


