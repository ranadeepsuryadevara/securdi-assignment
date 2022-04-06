import os
import subprocess

cp = "sudo apt install isc-dhcp-server"
cmd = cp
os.system(cmd)

cp = "cp /securdi-assignment/dhcp.conf /etc/dhcp"
cmd = cp
os.system(cmd)

cp = "cp /securdi-assignment/isc-dhcp-server /etc/default"
cmd = cp
os.system(cmd)

cp = "sudo systemctl restart isc-dhcp-server.service"
cmd = cp
os.system(cmd)

cp = "sudo systemctl status isc-dhcp-server.service"
cmd = cp
os.system(cmd)
