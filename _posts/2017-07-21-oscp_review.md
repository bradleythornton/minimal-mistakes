---
title:  "OSCP Review"
header: "OSCP Review"
categories: 
  - review
tags:
  - OSCP
---

There are tons of OSCP reviews floating around the web so I’ll keep the fluff to a minimum, to better make use of both our time. If you want to get to the meat and potatoes of what you should do, scroll down to the recommendations section.

## What is the OSCP

The most popular training provided by Offensive Security would be their Penetration Testing with Kali Linux (PWK). Upon completion of the PWK course and exam requirements, you’ll be awarded with the Offensive Security Certified Professional (OSCP) certification.

## Who should take it

It’s for those that have a thirst for security and actually practicing hacking techniques. This is a “learning by doing” course and if you have the **time** and **persistence** then you’ll be successful with it. I wouldn’t recommend this to someone new in the field or as a first security certification as I feel you should get your feet wet before you jump into the deep-end of the pool, but hey! You do you. 
A major piece of advice – If you don’t have the time to be consumed by this (say goodbye to your social life and house repairs) then I would recommend getting the courseware and the least amount of lab time to save yourself some money. You can study the material at your own pace and you can obtain lab time when you are ready.

## What you can expect to learn

*Short answer:*  
Here’s the [syllabus](https://www.offensive-security.com/documentation/penetration-testing-with-kali.pdf)  

*Personal answer:*  
Expect to be taken on a very personal journey through learning, enumeration, and exploitation. You’ll spend a lot of time googling, reading blogs, researching topics, and failing… but once you get a root shell on a machine, there’s no other feeling like it! To me, this training teaches you to “think like an attacker” and enumeration more than anything else. Of course you’ll pick up technical knowledge and skillsets along the way but learning to be resourceful, relentless, and to think outside of the box is something truly special that’s offered here.

## Pre-course recommendations

I basically have the same answer as everyone else that has blogged about it

 - A “Never give up” attitude because it will certainly test you
 - Time to dedicate to learning and following random rabbit holes
 - Basic knowledge of networking, Windows/Nix, Kali, common tools of the trade
 - You don’t have to be a programmer but learn some python ahead of time and be comfortable with making minor changes to existing code. 
 - Read some security books and blogs (you can see recommendations below)
 - **Do [VulnHub](https://www.vulnhub.com/) images!** Seriously, if you haven’t already then stop reading all the reviews and do some now before you even think about signing up. If you enjoy going through them then you’ll enjoy doing OSCP. It’s basically a free taste of it before you buy.

## Coursework

It comes with a 300+ page PDF and hours of videos. I highly recommend doing all of the exercises and any that you struggle with should be done multiple times and accompany outside research. The material is laid out well and in some cases the video has things that are not in the PDF’s so it’s good to do both. The material will give you a solid foundation but it’s only about 20% of what you’ll need to know to do the lab and exam machines. The real learning takes place on your own while you struggle to pop boxes and elevate privileges. You’ll be in all corners of the internet researching things and figuring out why a particular task isn’t being successful.

## The labs

Now this is where the real learning happens and what makes OSCP shine the brightest. You’ll have the opportunity to attack multiple networks and over 50 machines with various operating systems and configurations. The guys at Offensive Security really do a nice job of teaching you valuable lessons and building these machines. Many of the boxes can be exploited in multiple ways and varying degrees of difficulty so you have all the challenges you can imagine at your fingertips. The goal is to obtain proof.txt files off of compromised machines, obtain network-secret.txt files to unlock additional networks, and ultimately compromise the admin network. Needless to say, you won’t be bored with the options.

## The exam

The exam is a 24 hour practical exam followed by 24 hours to submit the report. During the first 24 hours, you’ll be expected to accumulate enough points (70) to pass out of 5 total machines of varying point values. I wouldn’t necessarily say that the exam machines are any more difficult than the majority of the lab machines, but it’s the time crunch that gets you. You really need a solid methodology and time management skills to pass the exam. I’m not sure of the fail rate but I feel very comfortable in saying that it’s probably high. Just about everyone that I’ve personally talked to has not passed on their first try (including myself). You shouldn’t let any of that deter you as I promise you’ll learn something out of the experience.

## Recommendations

#### Pre-course  
 - Attempt as many VulnHub images (see resource section) as you have time for. Try to do them on your own and if you get stuck then take a peek at the walkthroughs.
 - Ensure that you have time to sink into this endeavor and your significant other is onboard with it as well.
 - Read blogs to know what you are in for and lessons learned
 - Read as many security books/articles that you can get your hands on (see resource section)

#### Course  
 - Do all of the exercises and if any give you trouble redo the section again and research outside of the course
 - Perform the exercises where applicable to the lab environment, you’ll pop some boxes!
 - Keep in mind that this is simply the tip of the iceberg, most of what you’ll learn is in the lab and your own research
 - Do the buffer overflow section 4+ times and document the process completely in your own words

#### Labs  
 - Nothing is by chance, if it looks fishy then it most likely is.
 - Documentation is king, ensure you have a solid way of keeping notes as it will pay dividends later on
 - Enumerate, enumerate, enumerate, and enumerate some more. It’s not the sexiest part of the process but it's certainly a requirement
 - Revert the machine before you do a “real” attack against it
 - Use Metasploit to understand and become proficient with the tool but don’t rely on it. I started out using it a lot and then used it less and less as I went through the lab.
 - Focus on the low hanging fruit machines at first, the risky ports and gapingly wrong configurations. I usually had good luck with websites
 - Try to only go to the forums for hints when things get really bad, you won’t have it on the exam.
 - To keep up your motivation, take breaks and alternate between hard and easier machines.
 - Google everything and if something doesn’t work that should then it’s probably some minor detail and google may have your answer.
 - Be sure to re-start your enumeration process once you’ve got inside a machine to do privilege escalation.
 - Constantly be honing your enumeration methodology
 - Read every privilege escalation article you can possibly find as it’s usually where people have the most trouble.
 - Be sure to loot the machine fully as some machines are not directly exploitable and there are tons of Easter eggs and hints on them.

#### Exam  
 - Schedule the exam halfway through your lab time so you get a feel for the exam and know where your weak points are in time to hone in on them. It’s only $60 to do a retake which is significantly cheaper than most.
 - Create a plan and stick to it, schedule breaks
 - Have your cheat sheets ready and shells for various occasions
 - Don’t get stuck on any one machine rotate, every 3-4 hours
 - Write your report ahead of time so that you only need to add your exam notes in
 - Stick to your methodology and enumerate EVERYTHING
 - Start off with light port scans and work your way to more advanced ones
 - I had better luck with the higher point machines so I always started with those
 - Take a break of it all for a day or two before your exam

## Resources<a name="resource"></a>

#### Practice  

[Pushebx: Penetration Testing - Vulnerable - ISO](http://blog.pushebx.com/2011/03/penetration-testing-iso.html)  
[Practice CTFs](http://captf.com/practice-ctf/)  
[OverTheWire: Wargames](http://overthewire.org/wargames/)  
[Penetration Testing Mind Map](http://www.amanhardikar.com/mindmaps/Practice.html)  
[Vulnerable by Design](https://blog.g0tmi1k.com/2011/03/vulnerable-by-design/)  
[Exploit Exercises](https://exploit-exercises.com/)  
[Hack This Site!](https://www.hackthissite.org/pages/programs/programs.php)  

#### Vulnhub OSCP-like machines  

[SickOs: 1.2](SickOs:1.2https://www.vulnhub.com/entry/sickos-12,144/)  
[Kioptrix: 2014](Kioptrix:2014https://www.vulnhub.com/entry/kioptrix-2014-5,62/)  
[SkyTower: 1](SkyTower:1https://www.vulnhub.com/entry/skytower-1,96/)  
[FristiLeaks: 1.3](FristiLeaks:1.3https://www.vulnhub.com/entry/fristileaks-13,133/)  
[Stapler: 1](Stapler:1https://www.vulnhub.com/entry/stapler-1,150/)  
[Mr-Robot: 1](Mr-Robot:1https://www.vulnhub.com/entry/mr-robot-1,151/)  
[PwnLab: init](PwnLab:inithttps://www.vulnhub.com/entry/pwnlab-init,158/)  
[VulnOS: 2](VulnOS:2https://www.vulnhub.com/entry/vulnos-2,147/)  
[Brainpan: 1](Brainpan:1https://www.vulnhub.com/entry/brainpan-1,51/)  
[HackLAB: Vulnix](HackLAB:Vulnixhttps://www.vulnhub.com/entry/hacklab-vulnix,48/)  
[pWnOS: 2.0](pWnOS:2.0https://www.vulnhub.com/entry/pwnos-20-pre-release,34/)  

#### Reporting  

[Offensive Security - Sample Penetration Test Report](https://www.offensive-security.com/reports/sample-penetration-testing-report.pdf)  
[What is MagicTree](http://www.gremwell.com/what_is_magictree)  

#### Pivoting  

[Scenario Based Infrastructure Hacktics](http://www.fuzzysecurity.com/tutorials/13.html)  
[SSH Tunneling](http://exploit.co.il/networking/ssh-tunneling/)  
[Pink](http://www.pc-freak.net/blog/creating-ssh-tunnel-windows-plink/)  
[SSH Tunneling](http://superuser.com/questions/96489/an-ssh-tunnel-via-multiple-hops)  
[Transparent Multihop](http://sshmenu.sourceforge.net/articles/transparent-mulithop.html)  
[Tunneling](https://www.sans.org/reading-room/whitepapers/testing/tunneling-pivoting-web-application-penetration-testing-36117)  
[IP tables](http://www.linuxquestions.org/questions/linux-networking-3/iptables-forward-port-to-another-host-844467/)  
[SSH Meterpreter Pivoting Technqiues](https://highon.coffee/blog/ssh-meterpreter-pivoting-techniques/)  

#### Post Exploitation  

[Windows Post Exploitation](http://www.handgrep.se/repository/cheatsheets/postexploitation/WindowsPost-Exploitation.pdf)  
[Post Exploitation Using Meterpreter](https://www.exploit-db.com/docs/18229.pdf)  

#### Priv Esc - Win  

[Elevating Privileges](https://hackmag.com/security/elevating-privileges-to-administrative-and-further/)  
[Privilege escalation via weak services](http://travisaltman.com/windows-privilege-escalation-via-weak-service-permissions/)  
[MS Priv Esc](http://toshellandback.com/2015/11/24/ms-priv-esc/)  
[Windows Privilege Escalation Fundamentals](http://www.fuzzysecurity.com/tutorials/16.html)  
[Windows Privesc Check](https://github.com/pentestmonkey/windows-privesc-check)  
[Post Exploitation without a tty](http://pentestmonkey.net/blog/post-exploitation-without-a-tty)  
[WinEXE](http://www.desmoulins.fr/index_us.php?pg=informatique!linux!console!winexe)  
[DLL Hijacking](https://www.exploit-db.com/dll-hijacking-vulnerable-applications/)  
[Metasploit Unleashed ](https://www.offensive-security.com/metasploit-unleashed/portfwd/)  
[Udev Exploit Allows Local Privilege Escalation](http://www.madirish.net/370)  
[Create Admin user from command line](http://superuser.com/questions/515175/create-admin-user-from-command-line)  
[Windows Exploit Suggester](https://github.com/GDSSecurity/Windows-Exploit-Suggester/blob/master/windows-exploit-suggester.py)  
[UAC - What Pen Testers should know](http://blog.cobaltstrike.com/2014/03/20/user-account-control-what-penetration-testers-should-know/)  
[Bypassing UAC with Powershell](http://www.labofapenetrationtester.com/2015/09/bypassing-uac-with-powershell.html)  
[Win Exploit Suggester Intro](https://blog.gdssecurity.com/labs/2014/7/11/introducing-windows-exploit-suggester.html)  
[Infosec Reference](https://github.com/rmusser01/Infosec_Reference/)  

#### Priv Esc - Nix  

[Basic Linux Privilege Escalation](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/)  
[Udev](http://seclists.org/fulldisclosure/2009/Apr/att-198/udev.txt)  
[Enumeration & Privilege Escalation Cheat Sheet](http://www.rebootuser.com/?p=1623)  
[Linux Networking How To](http://oss.sgi.com/LDP/HOWTO/Net-HOWTO/x635.html)  
[AutoLocalPrivilegeEscalation](https://github.com/ngalongc/AutoLocalPrivilegeEscalation)  
[Escaping Restricted Shells](http://securebean.blogspot.com/2014/05/escaping-restricted-shell_3.html)  
[Fundamentals of Linux Privilege Escalation](http://www.slideshare.net/nullthreat/fund-linux-priv-esc-wprotections)  
[LinEnum](https://github.com/rebootuser/LinEnum)  
[LineEnum Enumeration Privilege Escalation Tool](http://www.darknet.org.uk/2014/11/linenum-linux-enumeration-privilege-escalation-tool/)  
[Inetd](https://debian-handbook.info/browse/stable/sect.inetd.html)  
[Introducing LinEnum](https://www.rebootuser.com/?p=1758)  

#### Password Cracking  

[John the Ripper Cheat Sheet](https://countuponsecurity.files.wordpress.com/2016/09/jtr-cheat-sheet.pdf)  
[Hashcat FAQ](https://hashcat.net/wiki/doku.php?id=frequently_asked_questions)  
[Password Crackers Cheat Sheet](https://www.unix-ninja.com/p/A_cheat-sheet_for_password_crackers)  
[Generating Wordlists](http://netsec.ws/?p=457)  

#### SQL  

[Accessing and Hacking MSSQL from Backtrack](http://www.iodigitalsec.com/accessing-and-hacking-mssql-from-backtrack-linux/)  
[Anatomy of an attack](http://resources.infosecinstitute.com/anatomy-of-an-attack-gaining-reverse-shell-from-sql-injection/)  
[Blind SQL Injection](https://www.exploit-db.com/docs/12622.pdf)  
[SQL Injection Cheat Sheet](http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet)  
[SQL Map](http://carnal0wnage.attackresearch.com/2011/03/sqlmap-with-post-requests.html)  

#### Payloads  

[Hex Values](http://stackoverflow.com/questions/1996184/all-possible-combination-for-an-hex-value-from-a-given-set-of-chars)  
[Generating Payloads](https://www.offensive-security.com/metasploit-unleashed/generating-payloads/)  
[Reverse Shell Cheat Sheet](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)  
[Reverse shell with bash](http://www.gnucitizen.org/blog/reverse-shell-with-bash/)  
[Veil](https://www.youtube.com/watch?v=v1OXNP_bl8U)  
[AutoMigrate](https://community.rapid7.com/thread/2082)  
[Reverse Shell Cheat Sheet](https://www.phillips321.co.uk/2012/02/05/reverse-shell-cheat-sheet/)  
[Offset-DB](http://offset-db.com/)  

#### Specific Exploits  

[LARES-ColdFusion](http://www.carnal0wnage.com/papers/LARES-ColdFusion.pdf)  
[Hacking a domain controller](http://web.archive.org/web/20141004091538/http:/www.slaughterjames.com/blog/2012/10/23/hacking-a-domain-controller-part-1-enumeration.html)  
[Mimikatz](https://adsecurity.org/?p=556)  
[Client Side Exploits](https://www.offensive-security.com/metasploit-unleashed/client-side-exploits/)  
[C Pointers](https://www.tutorialspoint.com/cprogramming/c_pointers.htm)  

#### Networking  

[ethereal tcpdump](http://alumni.cs.ucr.edu/~marios/ethereal-tcpdump.pdf)  
[tcpdump](https://danielmiessler.com/study/tcpdump/)  
[traffic accounting with ip tables](https://openvz.org/Traffic_accounting_with_iptables)  
[Netsh Commands for Windows Firewall](https://technet.microsoft.com/en-us/library/cc771920(v=ws.10).aspx)  

#### Misc  

[Tactical Exploitation](https://www.exploit-db.com/docs/172.pdf)  
[Help Beacon Peer](http://www.advancedpentest.com/help-beacon-peer)  
[Stealthy peer to peer](http://blog.cobaltstrike.com/2013/12/06/stealthy-peer-to-peer-cc-over-smb-pipes/)  
[Nishang](https://github.com/samratashok/nishang/tree/master/Escalation)  
[Powershell Empire](http://www.powershellempire.com/)  
[Pentest tips and tricks](https://jivoi.github.io/2015/07/01/pentest-tips-and-tricks/)  
[g0tmi1k github](https://github.com/g0tmi1k/)  
[Pen Testing Cheat Sheet](https://highon.coffee/blog/penetration-testing-tools-cheat-sheet/)  

#### Metasploit  

[MPC](https://github.com/g0tmi1k/mpc)  
[Converting Metasploit Modules](http://netsec.ws/?p=262)  
[msfconsol commands](https://www.offensive-security.com/metasploit-unleashed/msfconsole-commands/)  
[msfcli](https://www.offensive-security.com/metasploit-unleashed/msfcli/)  
[misc tools sheet](https://www.sans.org/security-resources/sec560/misc_tools_sheet_v1.pdf)  
[wirting meterpreter scripts](https://www.offensive-security.com/metasploit-unleashed/writing-meterpreter-scripts/)  

#### Recon  

[Information gathering](http://www.sersc.org/journals/JSE/vol5_no5_2008/6.pdf)  
[Intelligence gathering](http://www.pentest-standard.org/index.php/Intelligence_Gathering)  
[Top 10 nmap commands](http://bencane.com/2013/02/25/10-nmap-commands-every-sysadmin-should-know/)  
[Nmap cheat sheet](http://resources.infosecinstitute.com/nmap-cheat-sheet-discovery-exploits-part-2-advance-port-scanning-nmap-custom-idle-scan/)  
[DotDotPwn](https://media.blackhat.com/bh-us-11/Arsenal/BH_US_11_Nitrous_DotDotPwn_Slides.pdf)  
[Generates 8.3 File Names from Long File Names](https://support.microsoft.com/en-us/kb/142982)  
[Window version from file](http://security.stackexchange.com/questions/110673/how-to-find-windows-version-from-the-file-on-a-remote-system)  
[Enumerating user accounts](http://carnal0wnage.attackresearch.com/2007/07/enumerating-user-accounts-on-linux-and.html)  
[Nikto](https://scottlinux.com/2012/07/12/create-html-reports-with-nikto-web-server-scanner/)  
[httpscripting](https://curl.haxx.se/docs/httpscripting.html)  
[Nmap cheat sheet](http://resources.infosecinstitute.com/nmap-cheat-sheet-5-the-final-view-of-a-ninja-pentester/)  
[Netcat](https://www.digitalocean.com/community/tutorials/how-to-use-netcat-to-establish-and-test-tcp-and-udp-connections-on-a-vps)  
[Offsec PWB OSCP Experience](http://www.securitysift.com/offsec-pwb-oscp/)  

## Conclusion

I strongly recommend anyone take the OSCP if you have an interest in information security. In comparison to many of the other security certifications, this one gives you hands-on experience and isn’t just memorizing theories and definitions. It will give you a solid foundation in the penetration testing realm that can spring board into even further research and understanding. I’ve found that it gives people increased confidence to go out and participate in those CTF’s, tear apart that malware, and test exploits. An employer can rest assure, knowing that you don’t give up easily and you have shown **real effort** in the security space. After all this isn’t just a 9-5 to us, this is a hobby, a passion, a mindset, a calling.
