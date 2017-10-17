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
   startPort = int(raw_input("Enter Starting Port to Scan:"))
   endPort = int(raw_input("Enter Ending Port to Scan:"))

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
