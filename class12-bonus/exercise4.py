#!/usr/bin/env python

"""
4a. Create a new file named "test_netmiko.py". 
In this file, create a simple function that connects to arista1.lasthop.io 
and returns the Netmiko connection object. 

4b. Add a test into "test_netmiko.py" where you verify the Netmiko find_prompt() method works properly. 
This test should use the Netmiko connection function that you created in Exercise 4a.

4c. Create a second test function named "test_show_version" where you verify the EOS software version 
(currently the software version value is "4.20.10M", but this is subject to change in the future). 
Verify both of your tests from Exercise 4b and 4c pass properly using "py.test -s -v".

4d. Copy your "test_netmiko.py" file into a file named "test_netmiko_fixture.py". 
Now refactor your new "test_netmiko_fixture.py" file. 
This new module should be the same as what you had in Exercise 4c except that 
you should make the Netmiko connection function a pytest fixture (with a scope of "module"). 
Additionally, you should use this fixture for both of your test functions. 
Execute both of your tests in "test_netmiko_fixture.py" and verify they pass properly using "py.test -s -v test_netmiko_fixture.py".
"""
