import os
import re
def get_mac_address(iface):
	data = os.popen('ifconfig ' + iface ).read()
	words = data.split()
	found = 0 
	location = 0
	index = 0
	for x in words:
		if re.match('\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', x):
			found = 1
			index = location
			break
		else:
			location = location + 1
	if found == 1:
		mac = words[index]
	else:
		mac = 'Mac not found'
	return mac

if __name__ == '__main__':
	print(get_mac_address('en1'))