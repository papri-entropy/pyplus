#!/usr/bin/env python

""" 
2. Expand the TextFSM template created in exercise1 such that you extract the Port, Status, Vlan, Duplex, Speed, and Type columns. 
For the purposes of this exercise you can ignore the 'Name' column and assume it will always be empty. 
The output of the FSM table should look similar to the following:

$ textfsm.py ex2_show_int_status.tpl ex2_show_int_status.txt 
...
FSM Table:
['PORT_NAME', 'STATUS', 'VLAN', 'DUPLEX', 'SPEED', 'PORT_TYPE']
['Gi0/1/0','notconnect','1','auto','auto','10/100/1000BaseTX']
['Gi0/1/1','notconnect','1','auto','auto','10/100/1000BaseTX']
['Gi0/1/2','notconnect','1','auto','auto','10/100/1000BaseTX']
['Gi0/1/3','notconnect','1','auto','auto','10/100/1000BaseTX']
"""


