#!/usr/bin/env python3
from lxml import etree

# from pprint import pprint
doc = etree.parse('jira_url_data.xml')
xml_root = doc.getroot().find('channel').findall('item')
i = 0
for i in range(len(xml_root)):
    # get data from xml file:
    # find and findall, the findall func is extactly match.
    id_text = xml_root[i].findall('key')[0].text
    status_text = xml_root[i].findall('status')[0].text
    sum_text = xml_root[i].findall('summary')[0].text
    reporter_text = xml_root[i].findall('reporter')[0].attrib['username']
    desc_text = xml_root[i].findall('description')[0].text
    proj_text = xml_root[i].findall('project')[0].attrib['key']
    print(id_text + ' | ' + status_text + ' | ' + reporter_text + ' | ' + sum_text)
