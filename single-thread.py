#!/usr/bin/env python3
import threading
from time import sleep
import time

def task1():
	print('Task 1 executed.')
	sleep(1)

def task2():
	print('Task 2 executed.')
	sleep(5)

print('single thread...')
starttime=time.time()
task1()
task2()
endtime=time.time()
totaltime=starttime - endtime
print('Spend:{0:.5f}' .format(totaltime))