#!/usr/bin/env python

"""
1a. Using the show_security_zones.xml file, 
read the file contents and parse the file using etree.fromstring(). 
Print out the newly created XML variable and also print out the variable's type. 
Your output should look similar to the following:

<Element zones-information at 0x7f3271194b48>
<class 'lxml.etree._Element'>
"""

from pprint import pprint
from lxml import etree

with open("show_security_zones.xml") as f:
    my_xml = f.read()

print("#" * 40)
print("Printing XML string data after reading the file")
print("#" * 40)

print(my_xml)
print(type(my_xml))

print("#" * 40)
print("Printing XML after parsing with etree.parse")
print("#" * 40)

my_xml_parse = etree.parse("show_security_zones.xml")
print(my_xml_parse)
print(type(my_xml_parse))

print("#" * 40)
print("Printing XML after parsing with etree.fromstring")
print("#" * 40)

my_xml_fromstr = etree.fromstring(my_xml)
print(my_xml_fromstr)
print(type(my_xml_fromstr))

