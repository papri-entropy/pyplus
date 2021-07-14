#!/usr/bin/env python

from getpass import getpass
import os

password = os.getenv("PYPLUS_PASS") if os.getenv("PYPLUS_PASS") else getpass()

cisco3 = {
    "hostname": "cisco3.lasthop.io",
    "device_type": "ios",
    "username": "pyclass",
    "password": password,
    "optional_args": {}
    }

arista1 = {
    "hostname": "arista1.lasthop.io",
    "device_type": "eos",
    "username": "pyclass",
    "password": password,
    "optional_args": {}
    }



