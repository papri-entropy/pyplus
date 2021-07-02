#!/usr/bin/env python

"""
2a. Using xmltodict, load the show_security_zones.xml file as a Python dictionary. 
Print out this new variable and its type. 
Note, the newly created object is an OrderedDict; not a traditional dictionary.
"""

from pprint import pprint
import xmltodict

with open("show_security_zones.xml") as f:
    xml_str = f.read().strip()

print(type(xml_str))

xml_data = xmltodict.parse(xml_str)

print("#" * 50)
print("Printing var after parsing with xmltodict.parse")
print("#" * 50)

pprint(xml_data)

print("#" * 50)
print("Printing type OrderedDict, not a traditional dict")
print("#" * 50)

print(type(xml_data))
