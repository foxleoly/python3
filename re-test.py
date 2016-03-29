#!/usr/local/bin/env python3
#import re
import os
import json
from pprint import pprint
#load json data from a file and convert to string
#data = open('test_data','r').read()
#load json data
#data_re = json.loads(data)
with open('test_data','r') as f:
	data = json.loads(f)

for issues in data.items():
	pprint("****"+str(issues))