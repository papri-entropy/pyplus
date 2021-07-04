#!/usr/bin/env python

"""
4b. Use the find() method to find the first "zones-security-zonename". 
Print out the zone name for that element (the "text" of that element).
"""

from pprint import pprint
from lxml import etree

with open("show_security_zones.xml") as f:
    xml_str = f.read().strip()

xml_data = etree.fromstring(xml_str)

xml_zon_sec_name_first = xml_data.find(".//zones-security-zonename")

print("Find tex of the first zones-security-zonename element")
print("-" * 40)
print(xml_zon_sec_name_first.text)

