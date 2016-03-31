#!/usr/local/bin/env python3
#import re
import os
import json
from pprint import pprint
#load json data from a file and convert to string
data = open('json_data','r').read()
data_json = json.loads(data)
i = 1
for i in range (data_json['maxResults']):
	print(dict(data_json['issues'][i])['key']+" | "+ data_json['issues'][i]['fields']['summary'])
	