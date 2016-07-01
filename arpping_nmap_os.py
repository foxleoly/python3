#!/usr/bin/env python3
from scapy.all import *
import os
import nmap
#import logging

#logging.basicConfig(filename='arp_ping.log', level=logging.DEBUG)


# fileLog = open('arping.log','w')

def arp_ping(net):
    raw = arping(net, timeout=2, verbose=False)
    raw_reslut = raw[0].res

    for i in range(len(raw_reslut)):
        arp_result_fields = raw_reslut[i][1][1].fields
        IPs= arp_result_fields['psrc']
#        print('IP addr: ' + arp_result_fields['psrc'] + '	is UP!	' + 'Mac addr:' + arp_result_fields['hwsrc'])
#        logging.info('This is RAW OUTPUT:\n')
#        logging.debug(raw)
#        logging.info('This is RAW_RESULT OUTPUT:\n')
#        logging.debug(raw_reslut)
#        logging.info('This is ARP_RESULT OUTPUT:\n')
#        logging.debug(arp_result_fields)
#        logging.info('\n')


# print('RAW************** \n\n',raw)
#	print('RAW*****RESLUT*********\n\n',raw_reslut)
#	print('ARP***********READ******\n\n',arp_result_fields)	
#	fileLog.write(str(raw_reslut))
if __name__ == '__main__':
    arp_ping('192.168.153.0/24')
