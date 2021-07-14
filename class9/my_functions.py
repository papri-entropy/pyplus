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
