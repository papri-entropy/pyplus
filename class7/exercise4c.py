#!/usr/bin/env python

"""
4c. Use the findall() method to find all occurrences of "zones-security". 
For each of these security zones, print out the security zone name 
("zones-security-zonename", the text of that element).
"""

from pprint import pprint
from lxml import etree

with open("show_security_zones.xml") as f:
    xml_str = f.read().strip()

xml_data = etree.fromstring(xml_str)

print("Finding all occurrences of 'zones-security'")
xml_zon_sec_all = xml_data.findall(".//zones-security")
print(xml_zon_sec_all)

print("Prining the zone names of each sec zones:")
for zone in xml_zon_sec_all:
    for ele in zone:
        if ele.tag == "zones-security-zonename":
            print(ele.text)
    

