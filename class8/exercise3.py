#!/usr/bin/env python

"""
3a. Open a connection to the srx2 device and acquire a configuration lock. 
Validate that the configuration session is indeed locked by 
SSH'ing into the device and attempting to enter configuration mode ("configure"). 
Reuse, the 'srx2' device definition from the jnpr_devices.py file that you created in exercise2.

You should receive a prompt similar to the following:

pyclass@srx2> configure
Entering configuration mode
Users currently editing the configuration:
  pyclass (pid 30316) on since 2019-03-08 18:30:51 PST
      exclusive

Add code to attempt to lock the configuration again. 
Gracefully handle the "LockError" exception (meaning the configuration is already locked).

3b. Use the "load" method to stage a configuration using a basic set command, 
for example, "set system host-name python4life".

3c. Print the diff of the current configuration with the staged configuration. 
Your output should look similar to the following:

[edit system]
-  host-name srx2;
+  host-name python4life;

3d. Rollback the staged configuration. Once again, print out the diff 
of the staged and the current configuration (which at this point should be None).
"""

from jnpr.junos import Device
from pprint import pprint
import jnpr_devices
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError

srx2_device = Device(**jnpr_devices.srx2)

srx2_device.open()
srx2_device.timeout = 60

cfg = Config(srx2_device)

cfg.lock()

try:
    cfg.lock()
    print("Lock acquired!")
except LockError:
    print("Device is already locked.")

cfg.load("set system host-name python4life", format="set", merge=True)

print("#" * 50)
print("Printing DIFFS between running and candidate configs: ")
print("#" * 50)
print(cfg.diff())

cfg.rollback(0)

print("#" * 50)
print("Printing DIFFS between running and candidate configs after rollback: ")
print("#" * 50)
print(cfg.diff())
