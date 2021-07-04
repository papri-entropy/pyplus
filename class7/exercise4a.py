#!/usr/bin/env python

"""
4a. Use the find() method to retrieve the first "zones-security" element. 
Print out the tag of this element and of all its children elements. 
Your output should be similar to the following:

Find tag of the first zones-security element
--------------------
zones-security

Find tag of all child elements of the first zones-security element
--------------------
zones-security-zonename
zones-security-send-reset
zones-security-policy-configurable
zones-security-interfaces-bound
zones-security-interfaces
"""

from pprint import pprint
from lxml import etree

with open("show_security_zones.xml") as f:
    xml_str = f.read().strip()

xml_data = etree.fromstring(xml_str)

xml_zon_sec_first = xml_data.find("zones-security")

print("Find tag of the first zones-security element")
print("-" * 40)
print(xml_zon_sec_first.tag)

print()

print("Find tag of all child elements of the first zones-security element")
print("-" * 40)
for child in xml_zon_sec_first.getchildren():
    print(child.tag)
