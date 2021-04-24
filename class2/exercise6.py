#!/usr/bin/env python

"""
6. Using SSH and netmiko connect to the Cisco4 router. 
In your device definition, specify both an 'secret' and a 'session_log'. 
Your device definition should look as follows:

password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

Execute the following sequence of events using Netmiko:
a. Print the current prompt using find_prompt()

b. Execute the config_mode() method and print the new prompt using find_prompt()

c. Execute the exit_config_mode() method and print the new prompt using find_prompt()

d. Use the write_channel() method to send the 'disable' command down the SSH channel. 
Note, write_channel is a low level method so it requires that you add a newline to the end of your 'disable' command.

e. time.sleep for two seconds and then use the read_channel() method to read the data that is currently available on the SSH channel. 
Print this to the screen.

f. Execute the enable() method and print your now current prompt using find_prompt(). 
The enable() method will use the 'secret' defined in your device definition. 
This 'secret' is the same as the standard lab password.

g. After you are done executing your script, look at the 'my_output.txt' file to see what is included in the session_log.
"""

from pprint import pprint
from netmiko import ConnectHandler
from getpass import getpass
import os
import time
from datetime import datetime

password = os.getenv("PYPLUS_PASS") if os.getenv("PYPLUS_PASS") else getpass()


cisco4 = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt",
}

net_connect = ConnectHandler(**cisco4)

print(net_connect.find_prompt())
config_mode = net_connect.config_mode()
print(net_connect.find_prompt())
exit_config_mode = net_connect.exit_config_mode()
print(net_connect.find_prompt())
write_channel_disale = net_connect.write_channel("disable\n")
time.sleep(2)
read_channel = net_connect.read_channel()
print(read_channel)
execute_enable = net_connect.enable()
print(net_connect.find_prompt())
net_connect.disconnect()



