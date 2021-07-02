#!/usr/bin/env python

"""
1b. Using your XML variable from exercise 1a, 
print out the entire XML tree in a readable format 
(ensure that the output string is a unicode string).
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

my_xml_tostr = etree.tostring(my_xml_fromstr).decode()
print(my_xml_tostr)
print(type(my_xml_tostr))
