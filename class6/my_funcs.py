import yaml
from getpass import getpass

def read_yaml(inventory):
    password = getpass()
    with open(inventory) as f:
        data = yaml.load(f)
    for k in data:
        data[k]["password"] = password
    return data

def arp_output(output):
    arp_dict = dict()

    for arp_entry in output[0]["result"]["ipV4Neighbors"]:
        ip = arp_entry["address"]
        mac = arp_entry["hwAddress"]
        arp_dict[ip] = mac
    return arp_dict

    
