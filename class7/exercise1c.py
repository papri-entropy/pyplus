#!/usr/bin/env python

"""
1c. Print out the root element tag name (this tag should have a value of "zones-information"). 
Print the number of child elements of the root element (you can retrieve this using the len() function).
"""

from pprint import pprint
from lxml import etree

with open("show_security_zones.xml") as f:
    my_xml = f.read().strip()

print("#" * 40)
print("Printing XML after parsing with etree.fromstring")
print("#" * 40)

my_xml_fromstr = etree.fromstring(my_xml)
print(my_xml_fromstr)
print(type(my_xml_fromstr))

print("#" * 40)
print("Printing root element tag name")
print("#" * 40)

print(my_xml_fromstr.tag)

print("#" * 40)
print("Printing the number of child elements of the root element")
print("#" * 40)

print(len(my_xml_fromstr.getchildren()))
print(len(my_xml_fromstr))
