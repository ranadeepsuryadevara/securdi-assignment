import os
import subprocess

codepath = " sudo apt-get update -y && sudo apt install isc-dhcp-server"
cmd = codepath
os.system(cmd)

codepath = " sudo mv /etc/dhcp/dhcpd.conf /etc/dhcp/dhcpd.conf.backup"
cmd = codepath
os.system(cmd)

codepath = " cd /etc/dhcp"
cmd = codepath
os.system(cmd)
file1 = open("dhcpd.conf", "a")  # append mode
file1.write("""# a simple /etc/dhcp/dhcpd.conf
default-lease-time 600;
max-lease-time 7200;
authoritative;
 
subnet 192.168.1.0 netmask 255.255.255.0 {
 range 192.168.1.100 192.168.1.200;
 option routers 192.168.1.254;
 option domain-name-servers 192.168.1.1, 192.168.1.2;
#option domain-name "mydomain.example";
}
 \n""")
file1.close()

codepath = "cd /etc/default"
cmd = codepath
os.system(cmd)
file1 = open("isc-dhcp-server", "a")  # append mode
file1.write("INTERFACESv4="eth0" \n")
file1.close()


codepath = " sudo systemctl restart isc-dhcp-server.service"
cmd = codepath
os.system(cmd)

codepath = " sudo systemctl status isc-dhcp-server.service"
cmd = codepath
os.system(cmd)

print("DHCP Has been successfully installed and Configured")


