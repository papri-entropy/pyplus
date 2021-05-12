#!/usr/bin/env python

"""
6. Parse the following 'show ip bgp summary' output (see link below). 
From this output, extract the following fields: Neighbor, Remote AS, Up_Down, and State_PrefixRcvd. 
Also include the Local AS and the BGP Router ID in each row of the tabular output (hint: use filldown for this). 
Note, in order to simplify this problem only worry about the data shown in the output 
(in other words, don't worry about all possible values that could be present in the output).

Second hint: remember there is an implicit 'EOF -> Record' at the end of the template (by default).

https://github.com/ktbyers/pyplus_course/blob/master/class4/exercises/ex6_show_ip_bgp_summary.txt
"""
