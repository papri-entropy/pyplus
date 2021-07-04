#!/usr/bin/env python

"""
5a. Load the show_version.xml file (originally from a Cisco NX-OS device) 
using the etree.fromstring() method. Note this XML document, unlike the previous documents, 
contains the document encoding information. Because the document encoding is at the top of the file, 
you will need to read the file using "rb" mode (the "b" signifies binary mode). 
Print out the the namespace map of this XML object. 
You can accomplish this by using the .nsmap attribute of your XML object.
"""

from pprint import pprint
from lxml import etree

with open("show_version.xml", "rb") as f:
    xml_str = f.read().strip()

xml_data = etree.fromstring(xml_str)

print(f"Printing the namespace map:\n {xml_data.nsmap }")

