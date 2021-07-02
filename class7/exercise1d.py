#!/usr/bin/env python

"""
1d. Using both direct indices and the getchildren() method, 
obtain the first child element and print its tag name. 
"""

from pprint import pprint
from lxml import etree

with open("show_security_zones.xml") as f:
    my_xml = f.read().strip()

my_xml_fromstr = etree.fromstring(my_xml)

print("#" * 40)
print("Printing the first child element tag name")
print("#" * 40)

print("Print the child tag using getchildren()")
print(my_xml_fromstr.getchildren()[0].tag)

print("Print the child tag using list indices")
print(my_xml_fromstr[0].tag)
