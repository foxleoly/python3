#!/usr/bin/env python3
#the script to find the mac address in mac-filter section.
#	
#import the lxml lib
from lxml import etree as lt
#load the xml file
xml_doc = lt.parse('131_config.xml')
#set the xml root
xml_mac_filter = xml_doc.getroot().findall('mac-acl')
xml_intf = xml_doc.getroot().findall('interface')
xml_sn = xml_doc.getroot().find('system').find('serial-number').text
xml_lastboot = xml_doc.getroot().find('system').find('lastboot').text
xml_model = xml_doc.getroot().find('system').find('model').text
xml_base_mac = xml_doc.getroot().find('system').find('base-mac').text
xml_system_time = xml_doc.getroot().find('system').find('system-time').text
xml_username = xml_doc.getroot().find('system').find('username').text
xml_product_id = xml_doc.getroot().find('device-info').find('product-id').text
#parse the xml file and find the mac address:
for i in range (len(xml_mac_filter)):
	print (xml_mac_filter[i].find('mac').text)

for j in range (8,len(xml_intf)):
	print (xml_intf[j].find('ssid').text)
#print('\n','The total Mac:',len(xml_root_mac))

