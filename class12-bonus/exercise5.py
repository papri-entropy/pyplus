#!/usr/bin/env python

"""
5a. In a new directory named test_ex5, create a file named "conftest.py". 
In this file, copy the Netmiko connection function that you used as a fixture in the previous exercise.

5b. In a second file named "test_netmiko_conftest.py", re-create the same two test functions used in exercise4 
(test_prompt, and test_show_version). Ensure those test functions are using the fixture from conftest.py. 
Execute "py.test -s -v" in this directory and verify your tests pass properly.

5c. Add a finalizer to your fixture such that Netmiko gracefully closes the SSH session 
at the end of all your tests. Verify all of your tests still pass using "py.test -s -v".
"""
