#!/usr/bin/env python

"""
1e. Create a variable named "trust_zone". 
Assign this variable to be the first "zones-security" element in the XML tree. 
Access this newly created variable and print out the text of the 
"zones-security-zonename" child.
"""

from pprint import pprint
from lxml import etree

with open("show_security_zones.xml") as f:
    my_xml = f.read().strip()

my_xml_fromstr = etree.fromstring(my_xml)

trust_zone = my_xml_fromstr.getchildren()[0]

for child in trust_zone:
    if child.tag == "zones-security-zonename":
        print(child.text)

