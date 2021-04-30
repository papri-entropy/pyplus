#!/usr/bin/env python

"""
 1. Using the below ARP data, create a five element list. 
Each list element should be a dictionary with the following keys: 
"mac_addr", "ip_addr", "interface". 
At the end of this process, you should have five dictionaries contained inside a single list.

Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

from pprint import pprint

my_list = list()

arp_data = """
Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0
"""

for line in arp_data.splitlines():
    if 'Internet' not in line:
        continue
    else:
        my_dict = dict()
        my_dict['mac_addr'] = line.split()[3]
        my_dict['ip_addr'] = line.split()[1]
        my_dict['interface'] = line.split()[5]
        my_list.append(my_dict)

pprint(my_list)
    


