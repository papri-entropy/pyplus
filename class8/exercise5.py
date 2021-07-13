#!/usr/bin/env python

"""
5a. Connect to the srx2 device. Using an RPC call, gather and pretty-print the "show version" information. 
Recall that you can retrieve RPC method name by running "show version | display xml rpc" argument. 
Also don't forget to convert the hyphens to underscores. Your output should match the following:

<software-information>
<host-name>srx2</host-name>
<product-model>srx110h2-va</product-model>
<product-name>srx110h2-va</product-name>
<jsr/>
<package-information>
<name>junos</name>
<comment>JUNOS Software Release [12.1X46-D35.1]</comment>
</package-information>
</software-information>

5b. Using a direct RPC call, gather the output of "show interfaces terse". 
Print the output to standard out.

5c. Modify the previous task to capture "show interface terse", but this time only for "fe-0/0/7". 
Print the output to standard out. 
Use normalize=True in the RPC method call to make the output more readable. 
You will also need to add pretty_print=True to the etree.tostring() call. 
Consequently, your code should be similar to the following:

xml_out = dev.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
print(etree.tostring(xml_out, pretty_print=True, encoding="unicode"))
"""

from pprint import pprint
from jnpr.junos import Device
import jnpr_devices
from lxml import etree


if __name__=="__main__":

    srx2_device = Device(**jnpr_devices.srx2)

    srx2_device.open()

    print("#" * 50)
    print("Printing 'show version' output: ")
    print("#" * 50)

    sh_ver_xml_out = srx2_device.rpc.get_software_information()
    print(etree.tostring(sh_ver_xml_out, pretty_print=True, encoding="unicode"))

    print("#" * 50)
    print("Printing 'show interfaces terse' output: ")
    print("#" * 50)

    int_terse_xml_out = srx2_device.rpc.get_interface_information(terse=True, normalize=True)
    print(etree.tostring(int_terse_xml_out, pretty_print=True, encoding="unicode"))

    print("#" * 50)
    print("Printing 'show interfaces terse fe-0/0/7' output: ")
    print("#" * 50)

    int_fe_007_xml_out = srx2_device.rpc.get_interface_information(interface_name="fe-0/0/7", terse=True, normalize=True)
    print(etree.tostring(int_fe_007_xml_out, pretty_print=True, encoding="unicode"))
