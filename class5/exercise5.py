#!/usr/bin/env python

"""
5. Start with the full running-config from cisco3.lasthop.io as a base template 
(for example 'cisco3_config.j2'). 
Modify this base template such that you use Jinja2 include statements 
to pull in sub-templates for the NTP servers, the AAA configuration, and for the clock settings.

Your base template should have the following items (in the proper locations):

{% include 'aaa.j2' %}

{% include 'clock.j2' %}

{% include 'ntp.j2' %}

The child templates being pulled in should contain the NTP configuration, 
the AAA configuration, and the clock configuration. 
The two NTP servers, the timezone, timezone_offset, and timezone_dst 
(daylight savings timezone name) should be variables in these child templates.

The output from this should be the full configuration which is basically identical to the current running configuration on cisco3.lasthop.io.
"""

from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader('./templates')

cisco3_config = {"ntp_server1": "130.126.24.24", "ntp_server2": "152.2.21.1", "timezone": "PST", "timezone_offset": "-8 0", "timezone_dst": "PDT"} 

template_file = 'cisco3_config.j2'
template = env.get_template(template_file)
output = template.render(**cisco3_config)

print(output)


