#!/usr/bin/env python

"""
7. Using your TextFSM template and the 'show interface status' data from exercise2, 
create a Python program that uses TextFSM to parse this data. 
In this Python program, read the show interface status data from a file 
and process it using the TextFSM template. 
From this parsed-output, create a list of dictionaries. 
The program output should look as follows:

$ python ex7_show_int_status.py 

[{'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/0',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/1',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/2',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/3',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'}]
"""

from pprint import pprint
import textfsm

template_file ="ex2_show_int_status.tpl"
template = open(template_file)

with open("ex2_show_int_status.txt") as f:
    raw_text_data = f.read()

# The argument 'template' is a file handle and 'raw_text_data' is a string.

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)

template.close

print("\nPrint the header row which could be used for dictionary construction")
print(re_table.header)
print("\nOutput Data: ")
pprint(data)
print() 

data_headers = re_table.header

intf_list = list()

for intf in data:
    intf_dict = dict()
    for i in range(6):
        intf_dict[data_headers[i]] = intf[i]
    intf_list.append(intf_dict)

print()
pprint(intf_list)
print()

"""
Imagine that you have the following list.

keys = ['name', 'age', 'food']
values = ['Monty', 42, 'spam']

What is the simplest way to produce the following dictionary?

a_dict = {'name': 'Monty', 'age': 42, 'food': 'spam'}

Like this:

keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print(dictionary) # {'a': 1, 'b': 2, 'c': 3}

Voila :-) The pairwise dict constructor and zip function are awesomely useful.

Applying this technique to our exercise:

for intf in data:
	intf_dict = dict(zip(data_headers, intf))
	intf_list.append(intf_dict)

"""
