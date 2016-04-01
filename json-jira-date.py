#!/usr/local/bin/env python3
#import re
import os
import json
#from pprint import pprint
#The json data can be pretty display on screen if using pprint
#load json data from a file and convert to string
#the file name "json_data"
data = open('json_data','r').read()
data_json = json.loads(data)
i = 1
for i in range (data_json['maxResults']):
	print(dict(data_json['issues'][i])['key']+" | "+ data_json['issues'][i]['fields']['summary'])
	