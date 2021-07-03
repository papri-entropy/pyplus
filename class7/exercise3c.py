#!/usr/bin/env python

"""
3c. Optional - create a second function that uses xmltodict to read and parse a filename that you pass in. 
This function should support a "force_list" argument that is passed to xmltodict.parse(). 
Reminder, the force_list argument of xmltodict takes a dictionary 
where the dictionary key-name is the XML element that is required to be a list. For example:

force_list={"zones-security": True}

Use this new function to parse the "show_security_zones_single_trust.xml". 
Verify the Python data type is now a list for the ['zones-information']['zones-security'] element.
"""

from pprint import pprint
import xmltodict

def xml_read(filename):
    with open(filename) as f:
        xml_str = f.read().strip()
    xml_data = xmltodict.parse(xml_str)
    return xml_data

def xml_read_forcelist(filename, forcelist):
    with open(filename) as f:
        xml_str = f.read().strip()
    xml_data = xmltodict.parse(xml_str, force_list={forcelist: True})
    return xml_data

sec_zones = xml_read("show_security_zones.xml")
sec_zones_trust = xml_read_forcelist(filename="show_security_zones_trust.xml", forcelist="zones-security")

print("#" * 50)
pprint(sec_zones['zones-information']['zones-security'])
print(type(sec_zones['zones-information']['zones-security']))
print("#" * 50)
pprint(sec_zones_trust['zones-information']['zones-security'])
print(type(sec_zones_trust['zones-information']['zones-security']))
print("#" * 50)

