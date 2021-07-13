#!/usr/bin/env python

"""
4a. Using the previously created jnpr_devices.py file, 
open a connection to srx2 and gather the current routing table information.

4b. Using PyEZ stage a configuration from a file. 
The file should be "conf" notation. 
This configuration should add two static host routes (routed to discard). 
These routes should be from the RFC documentation range of 203.0.113.0/24 
(picking any /32 in that range should be fine). 
Use "merge=True" for this configuration. For example:

routing-options {
    static {
        route 203.0.113.5/32 discard;
        route 203.0.113.200/32 discard;
    }
}

4c. Reusing your gather_routes() function from exercise2, 
retrieve the routing table before and after you configuration change. 
Print out the differences in the routing table (before and after the change). 
To simplify the problem, you can assume that the only change will be *additional* routes added by your script.

4d. Using PyEZ delete the static routes that you just added.
You can use either load() and set operations or 
load() plus a configuration file to accomplish this.
"""

from pprint import pprint
from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from jnpr.junos.utils.config import Config
import jnpr_devices
from exercise2 import gather_routes

def print_rib(RIB_TABLE, TIME):

    print("#" * 50)
    print(f"ROUTING TABLE {TIME} THE TKT CHANGE: ")
    print("#" * 50)

    for k, v in RIB_TABLE.items():
        print("-" * 50)
        print(f"Route Entry: {k}")
        print(f"Route {k} attributes:")
        print(v)
        print()

def routes_diff(routes_before, routes_after):

    ROUTES_SET_DIFF = set(routes_after) - set(routes_before)

    ROUTES_LIST_DIFF = list(ROUTES_SET_DIFF)

    print("#" * 50)
    print("ROUTES THAT WERE ADDED: ")
    print("#" * 50)
    print(ROUTES_LIST_DIFF)
    print()

if __name__=="__main__":

    srx2_device = Device(**jnpr_devices.srx2)

    srx2_device.open()

    srx2_device.timeout = 60

# Checking the RIB before the change

    rib_table = gather_routes(srx2_device)

    print_rib(rib_table, "BEFORE")    

# Inventory Routes before the change

    ROUTES_BEFORE = list()

    for k in rib_table.keys():

        ROUTES_BEFORE.append(k)

# Adding the static routes

    cfg_static_routes = Config(srx2_device)

    cfg_static_routes.lock()  

    cfg_static_routes.load(path="static_routes.conf", format="text", merge=True)

    cfg_static_routes.commit()

# Checking the RIB after the change 

    rib_table = gather_routes(srx2_device)

    print_rib(rib_table, "AFTER")    

# Inventory Routes after the change 

    ROUTES_AFTER = list()

    for k in rib_table.keys():

        ROUTES_AFTER.append(k)

# DIFF Routes before vs after

    routes_diff(ROUTES_BEFORE, ROUTES_AFTER)

# Rolling back the change

    cfg_static_routes.load("delete routing-options static route 203.0.113.4/32", format="set", merge=True)
    cfg_static_routes.load("delete routing-options static route 203.0.113.44/32", format="set", merge=True)

    cfg_static_routes.commit()

    cfg_static_routes.unlock()  

# Checking the RIB after the ROLLBACK

    rib_table = gather_routes(srx2_device)

    print_rib(rib_table, "ROLLBACK")    
