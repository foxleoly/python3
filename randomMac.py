#!/usr/bin/env python3
import random
def GenRanMac():
	MacList = []
	for i in range(1,7):
		RanStr = "".join(random.sample("01234567890abcdef",2))
		MacList.append(RanStr)
	RanMac = ":".join(MacList)
	return RanMac

print (GenRanMac())
