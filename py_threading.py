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

print('Multi threading....')
starttime = time.time()
threads = []
t1 = threading.Thread(target=task1)
threads.append(t1)
t2 = threading.Thread(target=task2)
threads.append(t2)

for t in threads:
	t.setDaemon(True)
	t.start()

endtime=time.time();
totaltime=endtime - starttime;
print ('spend:{0:.5f}s' .format(totaltime))
print ('------------------')