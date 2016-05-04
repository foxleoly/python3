#!/usr/bin/env python3
#the script to find the mac address in mac-filter section.
#	
#import the lxml lib
from lxml import etree as lt
import sys
import random

#load the xml file
#xml_doc = lt.parse('131_config.xml')
try:
	xml_doc = lt.parse(sys.argv[1])
except Exception as e:
	print('Oh No! Pls enter the xml filename! %s' %e)
	sys.exit(2)
#set the xml root
xml_mac_filter = xml_doc.xpath('mac-acl/mac')
xml_sn = xml_doc.xpath('system/serial-number')[0].text
xml_lastboot = xml_doc.xpath('system/lastboot')[0].text
xml_model = xml_doc.xpath('system/model')[0].text
xml_base_mac = xml_doc.xpath('system/base-mac')[0].text
xml_system_time = xml_doc.xpath('system/system-time')[0].text
xml_username = xml_doc.xpath('system/username')[0].text
xml_product_id = xml_doc.xpath('device-info/product-id')[0].text
xml_dev_desc = xml_doc.xpath('device-info/device-description')[0].text
xml_mgnt_ip = xml_doc.xpath('management/static-ip')[0].text
xml_mgnt_mac = xml_doc.xpath('management/mac')[0].text
xml_mgnt_dhcp = xml_doc.xpath('management/dhcp-status')[0].text

##
print ('*************WAP Info**********')
print (' Product:',xml_dev_desc,'\n','Mgnt IP:',xml_mgnt_ip,'\n','Admin User:',xml_username,'\n','SN:',xml_sn)
print ('********************************\n')
print ('Mac addresses in mac-filter table:')
print ('*************MAc address**********')
##
#parse the xml file and find the mac address in mac filter
for i in range (len(xml_mac_filter)):
	print (xml_mac_filter[i].text)
print ('****************END***************')
##Genrate mac add entry for test:
# the example as below:
#<mac-acl name="default">
#<mac>68:a8:6d:33:6f:86</mac>
#</mac-acl>
# the def is to generate random mac address:
def GenRanMac():
	MacList = []
	for i in range(1,7):
		RanStr = "".join(random.sample("01234567890abcdef",2))
		MacList.append(RanStr)
	RanMac = ":".join(MacList)
	return RanMac


for i in range (1,10):
	print ('<mac-acl name="default">')
	print ('<mac>'+GenRanMac()+'</mac>')
	print ('</mac-acl>')
#for j in range (8,len(xml_intf)):
#	print (xml_intf[j].find('ssid').text)
#print('\n','The total Mac:',len(xml_root_mac))

