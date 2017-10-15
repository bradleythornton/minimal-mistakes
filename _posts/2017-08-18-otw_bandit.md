---
title:  "OverTheWire: Bandit Solutions"
header: "OverTheWire: Bandit Solutions"
categories: 
  - walkthroughs
tags:
  - overthewire
---

If you’re looking to hone some of your shell skills then the [OverTheWire: Bandit](http://overthewire.org/wargames/bandit/) series is certainly a step in the right direction. By the time you finish, you should be comfortable SSH’ing into machines, navigating the file system, and even a little bit of bash scripting. I thought it was a lot of fun and look forward to completing their other challenges.  

## Level 0:

The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.  

```console
root@kali:~# ssh bandit0@bandit.labs.overthewire.org -p 2220
```

## Level 0 -> 1:

The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level to continue.  

```console
bandit0@bandit:~$ ls
readme
bandit0@bandit:~$ cat readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

Type `exit` and SSH back into the machine with `ssh bandit1@bandit.labs.overthewire.org -p 2220`, be sure to change the user ID (in front of the @ symbol) to whichever level is appropriate for the level you which to work on. You would then use the flag that you found as the password, in this case its “boJ9jbbUNNfktd78OOpsqOltutMc3MY1”.  

## Level 1 -> 2:

The password for the next level is stored in a file called - located in the home directory  

```console
bandit1@bandit:~$ ls 
-
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
```
Try using some other commands instead of cat such as `more`.  


## Level 2 -> 3:

The password for the next level is stored in a file called "spaces in this filename" located in the home directory

```console
bandit2@bandit:~$ ls
spaces in this filename
bandit2@bandit:~$ cat "spaces in this filename"
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

## Level 3 -> 4:

The password for the next level is stored in a hidden file in the inhere directory.  

```console
bandit3@bandit:~$ ls 
inhere
bandit3@bandit:~$ cd inhere
bandit3@bandit:~/inhere$ ls -al
total 12
drwxr-xr-x 2 root    root    4096 Sep 28 14:04 .
drwxr-xr-x 4 bandit3 bandit3 4096 Oct 14 13:39 ..
-rw-r----- 1 bandit4 bandit3   33 Sep 28 14:04 .hidden
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
```

## Level 4 - >5:

The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

```console
bandit4@bandit:~$ ls 
inhere
bandit4@bandit:~$ cd inhere
bandit4@bandit:~/inhere$ ls -al
total 48
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file00
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file01
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file02
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file03
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file04
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file05
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file06
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file07
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file08
-rw-r----- 1 bandit5 bandit4   33 Sep 28 14:04 -file09
drwxr-xr-x 2 root    root    4096 Sep 28 14:04 .
drwxr-xr-x 4 bandit4 bandit4 4096 Oct 14 13:41 ..
bandit4@bandit:~/inhere$ file ./-*
./-file00: Non-ISO extended-ASCII text, with CR line terminators, with escape sequences
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

## Level 5 -> 6:

The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
human-readable  
1033 bytes in size  
not executable  

```console
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ cd inhere
bandit5@bandit:~/inhere$ ls 
maybehere00  maybehere02  maybehere04  maybehere06  maybehere08  maybehere10  maybehere12  maybehere14  maybehere16  maybehere18
maybehere01  maybehere03  maybehere05  maybehere07  maybehere09  maybehere11  maybehere13  maybehere15  maybehere17  maybehere19
bandit5@bandit:~/inhere$ find -size 1033c -type f
./maybehere07/.file2
bandit5@bandit:~/inhere$ cat ./maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

## Level 6 -> 7:

The password for the next level is stored somewhere on the server and has all of the following properties:

owned by user bandit7
owned by group bandit6
33 bytes in size

```console
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2>/dev/null                  
/var/lib/dpkg/info/bandit7.password
cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

## Level 7 -> 8:

The password for the next level is stored in the file data.txt next to the word millionth

```console
bandit7@bandit:~$ ls    
data.txt
bandit7@bandit:~$ cat data.txt | grep "millionth"
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

## Level 8 -> 9:

The password for the next level is stored in the file data.txt and is the only line of text that occurs only once.

```console
bandit8@bandit:~$ ls
data.txt
bandit8@bandit:~$ cat data.txt | sort | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

## Level 9 -> 10:

The password for the next level is stored in the file data.txt in one of the few human-readable strings, beginning with several ‘=’ characters.

```console
bandit9@bandit:~$ ls
data.txt
bandit9@bandit:~$ strings data.txt | grep "="
|========== the
,]=NB
@k<=
"m=g	
========== password
=r-3
========== is
mu=v.
<= V57
i=Hk>$B
========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
S1N=
PbgQ=Zp
=M Q
x3X}=
```

## Level 10 -> 11

The password for the next level is stored in the file data.txt, which contains base64 encoded data.

```console
bandit10@bandit:~$ ls
data.txt
bandit10@bandit:~$ cat data.txt | base64 --decode
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

## Level 11 -> 12:
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions.

```console
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt
Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh
bandit11@bandit:~$ cat data.txt |  tr '[A-Za-z]' '[N-ZA-Mn-za-m]'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

## Level 12 -> 13:
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. Then copy the datafile using cp, and rename it using mv (read the manpages!)

```console
bandit12@bandit:/tmp/thor$ ls
data
bandit12@bandit:/tmp/thor$ file data
data: gzip compressed data, was "data2.bin", from Unix, last modified: Thu Sep 28 14:04:06 2017, max compression
bandit12@bandit:/tmp/thor$ zcat data | file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/thor$ zcat data | bzcat | file -
/dev/stdin: gzip compressed data, was "data4.bin", from Unix, last modified: Thu Sep 28 14:04:06 2017, max compression
bandit12@bandit:/tmp/thor$ zcat data | bzcat | zcat | file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/thor$ zcat data | bzcat | zcat | tar xO | file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/thor$ zcat data | bzcat | zcat | tar xO | tar xO | file -
/dev/stdin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/thor$ zcat data | bzcat | zcat | tar xO | tar xO | bzcat | file -
/dev/stdin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/thor$ zcat data | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | file -
/dev/stdin: gzip compressed data, was "data9.bin", from Unix, last modified: Thu Sep 28 14:04:06 2017, max compression
bandit12@bandit:/tmp/thor$ zcat data | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat | file -
/dev/stdin: ASCII text
bandit12@bandit:/tmp/thor$ zcat data | bzcat | zcat | tar xO | tar xO | bzcat | tar xO | zcat 
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```

Once you log out, the new directory will be removed so no need to cleanup after yourself.  

## Level 13 -> 14:
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Note: localhost is a hostname that refers to the machine you are working on.

```console
bandit13@bandit:~$ ls
sshkey.private
bandit13@bandit:~$ ssh -i sshkey.private  bandit14@localhost -p 2220
Are you sure you want to continue connecting (yes/no)? yes
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

## Level 14 -> 15:
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.

```console
bandit14@bandit:~$ nc localhost 30000
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr
```

## Level 15 -> 16:
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.

Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage. Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…

```console
bandit14@bandit:~$ openssl s_client -ign_eof -connect localhost:30001
...[SNIPPED]...
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd
```

## Level 16 -> 17:
The credentials for the next level can be retrieved by submitting the password of the current level to a port on localhost in the range 31000 to 32000. First find out which of these ports have a server listening on them. Then find out which of those speak SSL and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.

```console
nmap -p 31000-32000 -sV  localhost

Starting Nmap 6.40 ( http://nmap.org ) at 2017-10-14 14:55 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00088s latency).
Other addresses for localhost (not scanned): 127.0.0.1
Not shown: 996 closed ports
PORT      STATE SERVICE VERSION
31046/tcp open  echo
31518/tcp open  msdtc   Microsoft Distributed Transaction Coordinator (error)
31691/tcp open  echo
31790/tcp open  msdtc   Microsoft Distributed Transaction Coordinator (error)
31960/tcp open  echo
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at http://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 41.40 seconds
bandit14@bandit:~$ openssl s_client -connect localhost:31790
CONNECTED(00000003)
..[SNIPPED]...
    Verify return code: 18 (self signed certificate)
---
cluFn7wTiGryunymYOu4RcffSxQluehd
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----
```

Next you'll need to log in with the key as user bandit17. You can do that with the below commands

```console
bandit14@bandit:~$ mkdir /tmp/thor
bandit14@bandit:~$ cd /tmp/thor
bandit14@bandit:/tmp/thor$ echo "-----BEGIN RSA PRIVATE KEY-----
> MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
> imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
> Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
> DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
> JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
> x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
> KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
> J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
> d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
> YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
> vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
> +TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
> 8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
> SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
> HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
> SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
> R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
> Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
> R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
> L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
> blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
> YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
> 77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
> dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
> vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
> -----END RSA PRIVATE KEY-----
> " > sshkey.private
bandit14@bandit:/tmp/thor$ chmod 600 sshkey.private 
bandit14@bandit:/tmp/thor$ ssh -i ./sshkey.private bandit17@localhost -p 2220
```

## Level 17 -> 18:
There are 2 files in the home directory: passwords.old and passwords.new. The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19.

```console
bandit17@bandit:~$ ls
passwords.new  passwords.old
bandit17@bandit:~$ diff passwords.new passwords.old 
42c42
< kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
---
> R3GQabj3vKRTcjTTISWvO1RJWc5sqSXO
```

The password is "kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd"

## Level 18 -> 19:
The password for the next level is stored in a file readme in the home directory. Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.

```console
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
bandit18@bandit.labs.overthewire.org's password: 
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

## Level 19 -> 20:
To gain access to the next level, you should use the setuid binary in the home directory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.

```console
bandit19@bandit:~$ ls
bandit20-do
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

## Level 20 -> 21:
There is a setuid binary in the home directory that does the following: it makes a connection to localhost on the port you specify as a command line argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Changes to the infrastructure made this level more difficult. You will need to figure out a way to launch multiple commands in the same Docker instance.

NOTE 2: Try connecting to your own network daemon to see if it works as you think

Terminal 1
```console
bandit20@bandit:~$ ls
suconnect
bandit20@bandit:~$ nc -l 55555 

```
Terminal 2

```console
bandit20@bandit:~$ ./suconnect 55555
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
```

Terminal 1
```console
GbKksEFF4yrVs6il55v6gwY5aVje5f0
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
```

Essentially you set up a listener on Terminal 1, connect to the listener on Terminal 2, enter in the password in Terminal 1 and it will return the correct password in the same terminal.


## Level 21 -> 22:
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

```console
bandit21@bandit:~$ cd /etc/cron.d/
bandit21@bandit:/etc/cron.d$ ls
cron-apt  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24  php5
bandit21@bandit:/etc/cron.d$ cat cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh 
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

## Level 22 -> 23:
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. If you are having problems understanding what it does, try executing it to see the debug information it prints.

```console
bandit22@bandit:~$ cd /etc/cron.d/
bandit22@bandit:/etc/cron.d$ ls
cron-apt  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24  php5
bandit22@bandit:/etc/cron.d$ cat cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
bandit22@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit23.sh
```
The contents of the script.  

```bash
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
```

```console
bandit22@bandit:/etc/cron.d$ echo I am user bandit23 | md5sum | cut -d ' ' -f 1
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:/etc/cron.d$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```

## Level 23 -> 24:
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…

```console
bandit23@bandit:~$ cd /etc/cron.d/
bandit23@bandit:/etc/cron.d$ ls  
cron-apt  cronjob_bandit22  cronjob_bandit23  cronjob_bandit24  php5
bandit23@bandit:/etc/cron.d$ cat cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
bandit23@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit24.sh
```

The contents of the script.  

```bash
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
	echo "Handling $i"
	timeout -s 9 60 ./$i
	rm -f ./$i
    fi
done
```

```console
bandit23@bandit:/etc/cron.d$ mkdir /tmp/thor
bandit23@bandit:/etc/cron.d$ cd /tmp/thor
bandit23@bandit:/tmp/thor$ nano script.sh
```

Code for your script.

```bash
#!/bin/bash

cat /etc/bandit_pass/bandit24 > tmp/thor/flag
```

```console
bandit23@bandit:/tmp/thor$ chmod 777 script.sh 
bandit23@bandit:/tmp/thor$ cp script.sh /var/spool/bandit24/
bandit23@bandit:/tmp/thor$ ls
script.sh flag
bandit23@bandit:/tmp/thor$ cat flag
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
```

## Level 24 -> 25:
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

```console
bandit24@bandit:~$ mkdir /tmp/thor
bandit24@bandit:~$ cd /tmp/thor
bandit24@bandit:/tmp/thor$ nano script.sh
```

Fill script.sh with the below code and save it.

```bash
#!/bin/bash
pass=UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ
for i in $(seq 0000 9999);
do
echo $pass' '$i | netcat localhost 30002 >> /tmp/thor/results
done
```

Once you run the script, keep in mind that it takes quite a while to brute force so you may want to go make a sandwich or something.

```console
bandit24@bandit:/tmp/thor$ chmod 755 script.sh 
bandit24@bandit:/tmp/thor$ ./script.sh
bandit24@bandit:/tmp/thor$ sort result | uniq -u

Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
```

## Level 25 -> 26:
Logging in to bandit26 from bandit25 should be fairly easy… The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.

```console
bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext
bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh

export TERM=linux

more ~/text.txt
exit 0
```

Shrink the console down so that less than 6 lines are showing.  

```console
bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost -p 2220
```

Press "V" and it will open up VIM

```console
:r /etc/bandit_pass/bandit26 [PRESS ENTER]
5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z
```
