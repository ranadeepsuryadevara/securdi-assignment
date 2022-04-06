import os
import subprocess

cp = "sudo apt-get update -y"
cmd = cp
os.system(cmd)

cp = "git clone https://github.com/ranadeepsuryadevara/securdi-assignment.git"
cmd = cp
os.system(cmd)

cp = "unzip securdi-assignment.zip"
cmd = cp
os.system(cmd)

cp = "python3 main.py"
cmd = cp
os.system(cmd)

cp = "sudo systemctl restart isc-dhcp-server.service"
cmd = cp
os.system(cmd)

cp = "sudo systemctl status isc-dhcp-server.service"
cmd = cp
os.system(cmd)
