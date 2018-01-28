# ZTP
Juniper ZTP for EX based on on serial number in this ay MAC address are no longer required 

required compunents 

Ubuntu 
isc-dhcpd for DHCP
Vsftpd for FTP 
Python3 
apache if web interface is required 

execute "sudo python3 ztp_configs.py" 

device needed to be either new or zeroized with auto-image enabled for this scrpit to work 

keep all templets and .py file in one folder including dhcpd file 


add following if device need to register it self to Junos Space by this config switch will add it self to junos space if it is monitoring for ZTP devices only thing needed to be defined in space is username and password which should match 


 event-options {
            generate-event { ztp-autoi time-interval 60; }
            policy ztp-autoi {
              events ztp-autoi;
              then {
                raise-trap;
