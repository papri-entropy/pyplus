#!/usr/bin/env python

"""
1f. Iterate through all of the child elements of the "trust_zone" variable. 
Print out the tag name for each child element.
"""

from pprint import pprint
from lxml import etree

with open("show_security_zones.xml") as f:
    my_xml = f.read().strip()

my_xml_fromstr = etree.fromstring(my_xml)

trust_zone = my_xml_fromstr.getchildren()[0]

print("#" * 80)
print("Looping directly")
print("#" * 80)

for child in trust_zone:
    print(child.tag)

print("#" * 80)
print("Looping using iterchildren")
print("#" * 80)

children = trust_zone.iterchildren()
for child in children:
    print(child.tag)
