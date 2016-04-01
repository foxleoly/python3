#!/usr/bin/env python3
from lxml import etree
#from pprint import pprint
doc = etree.parse('jira_url_data.xml')
xml_root = doc.getroot().find('channel').findall('item')[0]
for title in xml_root:
	print(etree.tostring(title))
