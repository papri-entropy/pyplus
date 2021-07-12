#!/usr/bin/env python

from getpass import getpass
import os

password = os.getenv("PYPLUS_PASS") if os.getenv("PYPLUS_PASS") else getpass()

srx2 = {
    "host": "srx2.lasthop.io",
    "user": "pyclass",
    "password": password
    }   

 
