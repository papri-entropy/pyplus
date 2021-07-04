#!/usr/bin/env python

"""
5b. Similar to earlier exercises, 
use the find() method to access the text of the "proc_board_id" element (serial number). 
As this XML object contains namespace data, you will need to use 
the {*} namespace wildcard in the find() method. 
Your find call should look as follows:

find(".//{*}proc_board_id")


The {*} is a namespace wildcard and says to match ALL namespaces.
"""

from pprint import pprint
from lxml import etree

with open("show_version.xml", "rb") as f:
    xml_str = f.read().strip()

xml_data = etree.fromstring(xml_str)

proc_board_id = xml_data.find(".//{*}proc_board_id").text

print(f"Prining the 'proc_board_id' elenment: {proc_board_id}")




