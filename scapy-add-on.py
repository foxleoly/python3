#!/usr/bin/env python3
import logging
logging.getLogger("scapy").setLevel(1)

from scapy.all import *
class myTestClass(Packet):
	name = "Test packet"
	fields_desc = [ ShortField("test1",1),
					ShortField("test2",2) ]

def make_test(x,y):
	return Ether()/IP()/myTestClass(test1=x,test2=y)

if __name__ == '__main__':
	interact(mydict=globals(), mybanner="Test add-on v3.4")