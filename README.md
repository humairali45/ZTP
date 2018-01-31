# ZTP
Juniper ZTP for EX based on on serial number in this ay MAC address are no longer required 

based on https://github.com/vloschiavo/ZTP project


1.	required compunents 

Ubuntu 
isc-dhcpd for DHCP
Vsftpd for FTP 
Python3 
apache if web interface is required 

2.	execute "sudo python3 ztp_configs.py" 
3.	
4.	device needed to be either new or zeroized with auto-image enabled for this scrpit to work 
	
5.	keep all templets and .py file in one folder including dhcpd file 
	
6.	FTP needed to be configured to allow anon user without password 
	
7.	two isc-dhcpd_template files are uploaded use it as per requirement rename the file to isc-dhcpd_template.js
	
8.	script is fetching following data from device_data2.csv file 

⦁	hostname "this will be the file name for the switch and same will be populated in dhcpd file"
⦁	
⦁	irb_ip "this is a vlan IP it is called in config tmplate hence needed to be set otherwise the config file will fail on commit if not required please remove it from template "
⦁	
⦁	irb_subnet "this is a vlan Subnet it is called  in config tmplate hence needed to be set otherwise the config file will fail on commit if not required please remove it from template "
⦁	
⦁	mgmt_ip " vme interface IP same as above if not required please remove it from template "
⦁	
⦁	mgmt_subnet " vme interface subnet same as above if not required please remove it from template "
⦁	
⦁	root_password " same as above"
⦁	
⦁	userid " same as above if not required please remove it from template "
⦁	
⦁	password " same as above if not required please remove it from template "
⦁	
⦁	uplink_port1 " same as above if not required please remove it from template "
⦁	
⦁	uplink_port2 " same as above if not required please remove it from template "
⦁	
⦁	
⦁	serial_number " this is required for identifying the switch required for dhcpd file genration"
⦁	
⦁	
⦁	no_port The Script is geting details from this field in for selecting template for now only 3 types are defined 12,24,48 if any other is required only template needed to be named for the same it is required to be defined or the script will fail.

9.	add following if device need to register it self to Junos Space by this config switch will add it self to junos space if it is monitoring for ZTP devices only thing needed to be defined in space is username and password which should match 


⦁	 event-options {
            generate-event { ztp-autoi time-interval 60; }
            policy ztp-autoi {
              events ztp-autoi;
              then {
                raise-trap;
