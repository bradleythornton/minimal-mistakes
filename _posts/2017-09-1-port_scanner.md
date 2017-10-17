---
title:  "Quick Python Port Scanner"
header: "Quick Python Port Scanner"
categories: 
  - tutorial
tags:
  - programming
  - scanner
  - python
---


I'm not a programmer by trade and only have limited experience by just hacking and slashing existing code to accommodate my needs for work/pen testing. In an attempt at increasing my knowledge in the area, I created a quick and simple port scanner. It’s by no means anywhere close to the functionality of nmap but it was a lot of fun making and I learned a lot during the process. I encourage you to create some scripts for anything you plan on doing more than once just for the sheer experience of it. Hit up the references at the bottom for further clarification or drop me some comments.  

## Python Code  

This has only been tested on the [Kali](https://www.kali.org/).  

```python
#!/usr/bin/env python
import socket, sys
from threading import Thread

# Easily changeable variables (you can extend the timeout length if necessary)
threads = []
timeout = 0.5

# Inputs & simple error handling
try:
   host = raw_input("Enter Target Host Address: ")
   hostIP = socket.gethostbyname(host)
   startPort = int(raw_input("Enter Starting Port to Scan: "))
   endPort = int(raw_input("Enter Ending Port to Scan: "))

except KeyboardInterrupt:
    print "\n\n[*]User Requested an Interrupt[*]"
    sys.exit()

except socket.gaierror:
    print "\n\n[*]Hostname unresolvable[*]"
    sys.exit()

except socket.error:
    print "\n\n[*]Unable to connect to target[*]"
    sys.exit()

# Scanning Banner
print "-" * 50
print "Scanning Target: ", hostIP
print "-" * 50

# Scanning and open port display
def scanner(port):
    	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.setdefaulttimeout(timeout)
	result = sock.connect_ex((hostIP, port))
	if result == 0:
	    print "[*] Port {}: Open".format(port)
	sock.close()

# Setup threading and calling the scan
for i in range(startPort, endPort+1):
	thread = Thread(target=scanner, args=(i,))
	threads.append(thread)
	thread.start()

[x.join() for x in threads]

# Completion Banner
print "-" * 50
print "Scanning completed!"
print "-" * 50
```
## Output/Example  

Internal Scan  
![Interal Scan](/assets/images/portscannerex2.jpg)  

External Scan  
![External Scan](/assets/images/portscannerex1.jpg)  

Ctrl + C Handling  
![CTRLC Handling](/assets/images/portscannerex3.jpg)  

Host Unreachable Handling  
![Host Unreachable](/assets/images/portscannerex4.jpg)  

## References  

[Python Socket Programming](https://docs.python.org/2/howto/sockets.html)  
[Sploit: How to Make a Python Port Scanner](https://null-byte.wonderhowto.com/how-to/sploit-make-python-port-scanner-0161074/)  
[Python For Beginners](http://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python)  
[Coderholic](http://www.coderholic.com/python-port-scanner/)  


