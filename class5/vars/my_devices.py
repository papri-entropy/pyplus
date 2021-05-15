from getpass import getpass 
password = getpass()
devices = {
        "nxos_devices": {
            "nxos1": {
                "config": {
                    "INTF": "Ethernet1/4",
                    "IP_ADDRESS": "10.1.99.1",
                    "NETMASK": 24,
                    "LOCAL_AS": 22,
                    "PEER_IP": "10.1.99.2"
                    },
                "connection": {
                    "host": "nxos1.lasthop.io",
                    "username": "pyclass",
                    "password": password,
                    "device_type": "cisco_nxos"
                    }
                    },
            "nxos2": {
                "config": {
                    "INTF": "Ethernet1/4",
                    "IP_ADDRESS": "10.1.99.2",
                    "NETMASK": 24,
                    "LOCAL_AS": 22,
                    "PEER_IP": "10.1.99.1"
                    },
                "connection": {
                    "host": "nxos2.lasthop.io",
                    "username": "pyclass",
                    "password": password,
                    "device_type": "cisco_nxos"
                    }
                    }
                    }
                    } 

