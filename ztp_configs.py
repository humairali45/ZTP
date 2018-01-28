#!/usr/bin/python

# Import the necessary modules
import csv
import sys
import sys
import subprocess
from getpass import getpass
from jinja2 import Template


# Set this variable to your dhcpd.conf path. 
# e.g.  dhcpd_file="/etc/dhcp/dhcpd.conf"

dhcpd_file="/etc/dhcp/dhcpd.conf"

# Set this variable to your web server path.  http://server_ip/config/ 
#path of your FTP/TFTP/HTTP server which is reachable by Devices
# e.g.  conf_path="/var/www/config/"
conf_path="/var/ftp/pub/"

# File name of your csv file
csv_filename="/tftpboot/device_data2.csv"

# Command to restart your DHCP daemon - unremark the next line
dhcpd_restart_command="sudo /etc/init.d/isc-dhcp-server restart"


device_data = csv.DictReader(open(csv_filename))

for row in device_data:
 

        data = row

        conffilename =  conf_path + row["hostname"] + ".conf";

        with open("junos_conf_template" + row["no_port"] + ".j2") as t_fh:
            t_format = t_fh.read()

        template = Template(t_format)

        fout = open(conffilename, 'w')

        fout.write((template.render(data)))
        fout.close()

        with open("isc-dhcpd_template.j2") as t2_fh:
            t2_format = t2_fh.read()
        template2 = Template(t2_format)

        with open(dhcpd_file, "a") as dhcpdconf:
                dhcpdconf.write(template2.render(data))

from subprocess import call
dhcpd_return_code = call(dhcpd_restart_command, shell=True)

