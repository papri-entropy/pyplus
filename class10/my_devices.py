from getpass import getpass
import os

password = os.getenv("PYPLUS_PASS") if os.getenv("PYPLUS_PASS") else getpass()

cisco3 = {
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
    "session_log": "cisco3_session_log"
}

arista1 = {
    "host": "arista1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "arista_eos",
    "global_delay_factor": 4,
    "session_log": "arista1_session_log"
}

arista2 = {
    "host": "arista2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "arista_eos",
    "global_delay_factor": 4,
    "session_log": "arista2_session_log"
}

srx2 = {
    "host": "srx2.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "juniper_junos",
    "session_log": "srx2_session_log"
}

devices = [cisco3, arista1, arista2, srx2]
