#!/usr/bin/env python

"""
2a. Create a Python module named jnpr_devices.py.
This Python module should contain a dictionary named "srx2".
This "srx2" dictionary should contain all of the key-value pairs
needed to establish a PyEZ connection.
You should use getpass() for the password handling.
You should import this "srx2" device definition for all
of the remaining exercises in class8.

2b. Create a Python program that creates a PyEZ Device connection to "srx2" 
(using the previously created Python module). 
Using this PyEZ connection and the RouteTable and ArpTable views 
retrieve the routing table and the arp table for srx2.

This program should have four separate functions:
1. check_connected() - Verify that your NETCONF connection is working. 
You can use the .connected attribute to check the status of this connection.
2. gather_routes() - Return the routing table from the device.
3. gather_arp_table() - Return the ARP table from the device.
4. print_output() - A function that takes the Juniper PyEZ Device object,
 the routing table, and the ARP table 
and then prints out the: hostname, NETCONF port, username, routing table, ARP table

This program should be structured such that 
all of the four functions could be reused in other class8 exercises.
"""

from jnpr.junos import Device
from pprint import pprint
import jnpr_devices
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.op.arp import ArpTable

def check_connected():

    conn_status = srx2_device.connected

    if conn_status:
        print("Device is successfully connected")
    else:
        print("Device failed to connect")
        sys.exit(1)

    return conn_status

def gather_routes(jnpr_device):
    rib_table = RouteTable(jnpr_device)
    rib_table = dict(rib_table.get().items())

    return rib_table

def gather_arp_table(jnpr_device):
    arp_table = ArpTable(jnpr_device)
    arp_table = dict(arp_table.get().items())

    return arp_table

def print_output(JNPR_DEV, RIB_TABLE, ARP_TABLE):

    print("#" * 50)
    print("DEVICE INFO: ")    
    print("#" * 50)

    print(f"Juniper device hostname: {JNPR_DEV.hostname}")

    print(f"Juniper device port: {JNPR_DEV.port}")

    print(f"Juniper device username: {JNPR_DEV.user}")

    print(f"NETCONF connection status is UP: {conn_status}")

    print("#" * 50)
    print("ROUTING TABLE: ")    
    print("#" * 50)
    
    for k, v in RIB_TABLE.items():
        print("-" * 50)
        print(f"Route Entry: {k}")
        print(f"Route {k} attributes:")
        print(v)
        print()

    print("#" * 50)
    print("ARP TABLE: ")
    print("#" * 50)

    print("-" * 50)
    pprint(ARP_TABLE)
    print()

if __name__=="__main__":    

    srx2_device = Device(**jnpr_devices.srx2)

    srx2_device.open()

    conn_status = check_connected()

    rib_table = gather_routes(srx2_device)

    arp_table = gather_arp_table(srx2_device)

    print_output(srx2_device, rib_table, arp_table)



