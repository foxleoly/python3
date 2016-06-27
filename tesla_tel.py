#!/usr/bin/env python3
import pexpect as pe
cmd = "telnet 10.75.166.235"
host_raw = pe.spawn(cmd)
host_raw.expect("Terminal-Server#", timeout=2)
host_raw.sendline("terminal length 0")
host_raw.expect("Terminal-Server#", timeout=2)
host_raw.sendline("sho ver")
host_raw.expect("Terminal-Server#")

host_raw.close()
print('all the command done!!')
