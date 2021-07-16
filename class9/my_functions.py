#!/usr/bin/env python

from napalm import get_network_driver

def napalm_conn(device):
    device_type = device.pop("device_type")
    driver = get_network_driver(device_type)
    device_conn = driver(**device)
    device_conn.open()

    return device_conn

def create_backup(conn_object):

    running_conf = conn_object.get_config()

    return running_conf 

def create_checkpoint(conn_object, checkpoint_name):

    checkpoint = conn_object._get_checkpoint_file()

    with open(checkpoint_name, "w") as f:
        f.write(checkpoint)

    return checkpoint

  
    
