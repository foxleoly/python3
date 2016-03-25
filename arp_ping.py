#!/usr/bin/python3

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
def arpping(network_prefix):
	result_raw = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=network_prefix),timeout=2,iface = 'en1', verbose=False)
	result_list = result_raw[0].res

	for i in range(len(result_list)):
		arp_result_fields = result_list[i][1][1].fields
		print('IP addr: ' + arp_result_fields['psrc'] + '	is UP!	'+ 'Mac addr:' + arp_result_fields['hwsrc'])

if __name__ == '__main__':
	arpping('192.168.3.0/24')