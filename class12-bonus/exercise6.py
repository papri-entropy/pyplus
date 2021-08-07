#!/usr/bin/env python

"""
6a. In GitHub, create a fork of the "pyplus_course" repository (https://github.com/ktbyers/pyplus_course).

6b. Go to Travis-CI (https://travis-ci.com), in the top right corner, click "Sign in with GitHub". 
Follow the prompts to authorize your account. 
Once completed, click the "Activate" button on your user Dashboard/Repositories page.

6c. Select ONLY the forked "pyplus_course" repository and click "Approve & Install".

6d. Clone the "pyplus_course" repository that you forked earlier into your account on the AWS lab system. 
Edit the README.md to include some additional text. 
Commit this change, and then push this change back into GitHub 
(reminder, you should now be working on your fork of this 'pyplus_course' repository; 
consequently, you should be pushing the change back to your fork).

6e. In the Travis-CI dashboard, you should now see a process starting or running. 
This build is executing commands that it has discovered in the ".travis.yml" file. 
If all goes well you should see the results of the build shortly.

6f. If you want to intentionally create a failure in Travis-CI, 
then add a file named "my_test.py" to the base of the pyplus_course repository. 
In this file, ensure there is a pycodestyle or black issue. 
For example, add a=22 with no spaces around the equals sign. 
Commit this file using Git. Push this file back into your pyplus_course repository. 
Travis-CI should now fail as both the 'pylama .' check and the 'black --check .' will fail.
"""
