#!/usr/bin/env python


from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass
import os
import datetime

class SSHConn:
    def __init__(self, host, username, password, device_type):
        self.host = host
        self.username = username
        self.password = password
        self.device_type = device_type

    def open(self):
        self.net_connect = ConnectHandler(host=self.host, username=self.username, password=self.password, device_type=self.device_type)
        print(self.net_connect.find_prompt())

    def version(self, cmd="show version"):
        output_ver  = self.net_connect.send_command(cmd, use_textfsm=True)
        print(output_ver)
        
if __name__=='__main__':
    password = os.getenv("PYPLUS_PASS") if os.getenv("PYPLUS_PASS") else getpass()

    cisco4_conn = SSHConn(host="cisco4.lasthop.io", username="pyclass", password=password, device_type="cisco_ios")
    cisco4_prompt = cisco4_conn.open()
    cisco4_ver = cisco4_conn.version()

