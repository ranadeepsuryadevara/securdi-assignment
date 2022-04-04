import os
import subprocess

cp = "sudo apt install isc-dhcp-server"
cmd = cp
os.system(cmd)

cp = "sudo mv /etc/dhcp/dhcpd6.conf /etc/dhcp/dhcpd6.conf.backup"
cmd = cp
os.system(cmd)

cp = "cd /etc/dhcp"
cmd = cp
os.system(cmd)

file_object = open('dhcpd6.conf', 'a')
# Append 'hello' at the end of file
file_object.write('''# a simple /etc/dhcp/dhcpd.conf
default-lease-time 600;
max-lease-time 7200;
authoritative;
 
subnet 192.168.1.0 netmask 255.255.255.0 {
 range 192.168.1.100 192.168.1.200;
 option routers 192.168.1.254;
 option domain-name-servers 192.168.1.1, 192.168.1.2;
#option domain-name "mydomain.example";
}''')
# Close the file
file_object.close()

cp = "cd /etc/default"
cmd = cp
os.system(cmd)

file_object = open('isc-dhcp-server', 'a')
# Append 'hello' at the end of file
file_object.write('INTERFACESv4="eth0"')
# Close the file
file_object.close()


cp = "sudo systemctl restart isc-dhcp-server.service"
cmd = cp
os.system(cmd)

cp = "sudo systemctl status isc-dhcp-server.service"
cmd = cp
os.system(cmd)
