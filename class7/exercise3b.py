#!/usr/bin/env python

"""
3b. Compare the Python "type" of the elements at ['zones-information']['zones-security']. 
What is the difference between the two data types? Why?
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
pprint(sec_zones['zones-information']['zones-security'])
print(type(sec_zones['zones-information']['zones-security']))
print("#" * 50)
pprint(sec_zones_trust['zones-information']['zones-security'])
print(type(sec_zones_trust['zones-information']['zones-security']))
print("#" * 50)

