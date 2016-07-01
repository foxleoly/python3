#!/usr/bin/env python3
import pexpect as pe

cmd = "telnet 10.75.166.235 2058"
default_pwd = "cisco"

host_res = pe.spawn(cmd)
host_res.expect("User Name:", timeout=2)
host_res.sendline(default_pwd)
host_res.expect("Password:", timeout=2)
host_res.sendline(default_pwd)
host_res.expect("SG350XG-24T#", timeout=2)
host_res.sendline("termi leng 0")
host_res.expect("SG350XG-24T#", timeout=2)
host_res.sendline("show ver")

data = host_res.before

host_res.close()
print('All Done!!')
