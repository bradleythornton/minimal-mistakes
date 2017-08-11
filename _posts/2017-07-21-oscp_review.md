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
 - Enumerate, enumerate, enumerate, and enumerate some more. It’s not the sexiest part it certainly a requirement
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

## Resources

Practice

[http://blog.pushebx.com/2011/03/penetration-testing-iso.html](http://blog.pushebx.com/2011/03/penetration-testing-iso.html)
[http://captf.com/practice-ctf/](http://captf.com/practice-ctf/)
[http://overthewire.org/wargames/](http://overthewire.org/wargames/)
[http://www.amanhardikar.com/mindmaps/Practice.html](http://www.amanhardikar.com/mindmaps/Practice.html)
[https://blog.g0tmi1k.com/2011/03/vulnerable-by-design/](https://blog.g0tmi1k.com/2011/03/vulnerable-by-design/)
[https://exploit-exercises.com/](https://exploit-exercises.com/)
[https://www.hackthissite.org/pages/programs/programs.php](https://www.hackthissite.org/pages/programs/programs.php)

Vulnhub OSCP-like machines

[SickOs: 1.2](https://www.vulnhub.com/entry/sickos-12,144/)
[Kioptrix: 2014](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)
[SkyTower: 1](https://www.vulnhub.com/entry/skytower-1,96/)
[FristiLeaks: 1.3](https://www.vulnhub.com/entry/fristileaks-13,133/)
[Stapler: 1](https://www.vulnhub.com/entry/stapler-1,150/)
[Mr-Robot: 1](https://www.vulnhub.com/entry/mr-robot-1,151/)
[PwnLab: init](https://www.vulnhub.com/entry/pwnlab-init,158/)
[VulnOS: 2](https://www.vulnhub.com/entry/vulnos-2,147/)
[Brainpan: 1](https://www.vulnhub.com/entry/brainpan-1,51/)
[HackLAB: Vulnix](https://www.vulnhub.com/entry/hacklab-vulnix,48/)
[pWnOS: 2.0](https://www.vulnhub.com/entry/pwnos-20-pre-release,34/)


Reporting

[https://www.offensive-security.com/reports/sample-penetration-testing-report.pdf](https://www.offensive-security.com/reports/sample-penetration-testing-report.pdf)
[http://www.gremwell.com/what_is_magictree](http://www.gremwell.com/what_is_magictree)

Pivoting

[http://www.fuzzysecurity.com/tutorials/13.html](http://www.fuzzysecurity.com/tutorials/13.html)
[http://exploit.co.il/networking/ssh-tunneling/](http://exploit.co.il/networking/ssh-tunneling/)
[http://www.pc-freak.net/blog/creating-ssh-tunnel-windows-plink/](http://www.pc-freak.net/blog/creating-ssh-tunnel-windows-plink/)
[http://superuser.com/questions/96489/an-ssh-tunnel-via-multiple-hops](http://superuser.com/questions/96489/an-ssh-tunnel-via-multiple-hops)
[http://sshmenu.sourceforge.net/articles/transparent-mulithop.html](http://sshmenu.sourceforge.net/articles/transparent-mulithop.html)
[https://www.sans.org/reading-room/whitepapers/testing/tunneling-pivoting-web-application-penetration-testing-36117](https://www.sans.org/reading-room/whitepapers/testing/tunneling-pivoting-web-application-penetration-testing-36117)
[http://www.linuxquestions.org/questions/linux-networking-3/iptables-forward-port-to-another-host-844467/](http://www.linuxquestions.org/questions/linux-networking-3/iptables-forward-port-to-another-host-844467/)
[https://highon.coffee/blog/ssh-meterpreter-pivoting-techniques/](https://highon.coffee/blog/ssh-meterpreter-pivoting-techniques/)

Post Exploitation

[http://www.handgrep.se/repository/cheatsheets/postexploitation/WindowsPost-Exploitation.pdf](http://www.handgrep.se/repository/cheatsheets/postexploitation/WindowsPost-Exploitation.pdf)
[https://www.exploit-db.com/docs/18229.pdf](https://www.exploit-db.com/docs/18229.pdf)

Priv Esc - Win

[https://hackmag.com/security/elevating-privileges-to-administrative-and-further/](https://hackmag.com/security/elevating-privileges-to-administrative-and-further/)
[http://travisaltman.com/windows-privilege-escalation-via-weak-service-permissions/](http://travisaltman.com/windows-privilege-escalation-via-weak-service-permissions/)
[http://toshellandback.com/2015/11/24/ms-priv-esc/](http://toshellandback.com/2015/11/24/ms-priv-esc/)
[http://www.fuzzysecurity.com/tutorials/16.html](http://www.fuzzysecurity.com/tutorials/16.html)
[https://github.com/pentestmonkey/windows-privesc-check](https://github.com/pentestmonkey/windows-privesc-check)
[http://pentestmonkey.net/blog/post-exploitation-without-a-tty](http://pentestmonkey.net/blog/post-exploitation-without-a-tty)
[http://www.desmoulins.fr/index_us.php?pg=informatique!linux!console!winexe](http://www.desmoulins.fr/index_us.php?pg=informatique!linux!console!winexe)
[https://www.exploit-db.com/dll-hijacking-vulnerable-applications/](https://www.exploit-db.com/dll-hijacking-vulnerable-applications/)
[https://www.offensive-security.com/metasploit-unleashed/portfwd/](https://www.offensive-security.com/metasploit-unleashed/portfwd/)
[http://www.madirish.net/370](http://www.madirish.net/370)
[http://superuser.com/questions/515175/create-admin-user-from-command-line](http://superuser.com/questions/515175/create-admin-user-from-command-line)
[https://github.com/GDSSecurity/Windows-Exploit-Suggester/blob/master/windows-exploit-suggester.py](https://github.com/GDSSecurity/Windows-Exploit-Suggester/blob/master/windows-exploit-suggester.py)
[http://blog.cobaltstrike.com/2014/03/20/user-account-control-what-penetration-testers-should-know/](http://blog.cobaltstrike.com/2014/03/20/user-account-control-what-penetration-testers-should-know/)
[http://www.labofapenetrationtester.com/2015/09/bypassing-uac-with-powershell.html](http://www.labofapenetrationtester.com/2015/09/bypassing-uac-with-powershell.html)
[https://blog.gdssecurity.com/labs/2014/7/11/introducing-windows-exploit-suggester.html](https://blog.gdssecurity.com/labs/2014/7/11/introducing-windows-exploit-suggester.html)
[https://github.com/rmusser01/Infosec_Reference/](https://github.com/rmusser01/Infosec_Reference/)

Priv Esc - Nix

[https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/](https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/)
[http://seclists.org/fulldisclosure/2009/Apr/att-198/udev.txt](http://seclists.org/fulldisclosure/2009/Apr/att-198/udev.txt)
[http://www.rebootuser.com/?p=1623](http://www.rebootuser.com/?p=1623)
[http://oss.sgi.com/LDP/HOWTO/Net-HOWTO/x635.html](http://oss.sgi.com/LDP/HOWTO/Net-HOWTO/x635.html)
[https://github.com/ngalongc/AutoLocalPrivilegeEscalation](https://github.com/ngalongc/AutoLocalPrivilegeEscalation)
[http://securebean.blogspot.com/2014/05/escaping-restricted-shell_3.html](http://securebean.blogspot.com/2014/05/escaping-restricted-shell_3.html)
[http://www.slideshare.net/nullthreat/fund-linux-priv-esc-wprotections](http://www.slideshare.net/nullthreat/fund-linux-priv-esc-wprotections)
[https://github.com/rebootuser/LinEnum](https://github.com/rebootuser/LinEnum)
[http://www.darknet.org.uk/2014/11/linenum-linux-enumeration-privilege-escalation-tool/](http://www.darknet.org.uk/2014/11/linenum-linux-enumeration-privilege-escalation-tool/)
[https://debian-handbook.info/browse/stable/sect.inetd.html](https://debian-handbook.info/browse/stable/sect.inetd.html)
[https://www.rebootuser.com/?p=1758](https://www.rebootuser.com/?p=1758)

Password Cracking

[https://countuponsecurity.files.wordpress.com/2016/09/jtr-cheat-sheet.pdf](https://countuponsecurity.files.wordpress.com/2016/09/jtr-cheat-sheet.pdf)
[https://hashcat.net/wiki/doku.php?id=frequently_asked_questions](https://hashcat.net/wiki/doku.php?id=frequently_asked_questions)
[https://www.unix-ninja.com/p/A_cheat-sheet_for_password_crackers](https://www.unix-ninja.com/p/A_cheat-sheet_for_password_crackers)
[http://netsec.ws/?p=457](http://netsec.ws/?p=457)

SQL

[http://www.iodigitalsec.com/accessing-and-hacking-mssql-from-backtrack-linux/](http://www.iodigitalsec.com/accessing-and-hacking-mssql-from-backtrack-linux/)
[http://resources.infosecinstitute.com/anatomy-of-an-attack-gaining-reverse-shell-from-sql-injection/](http://resources.infosecinstitute.com/anatomy-of-an-attack-gaining-reverse-shell-from-sql-injection/)
[https://www.exploit-db.com/docs/12622.pdf](https://www.exploit-db.com/docs/12622.pdf)
[http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet](http://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet)
[http://carnal0wnage.attackresearch.com/2011/03/sqlmap-with-post-requests.html](http://carnal0wnage.attackresearch.com/2011/03/sqlmap-with-post-requests.html)

Payloads

[http://stackoverflow.com/questions/1996184/all-possible-combination-for-an-hex-value-from-a-given-set-of-chars](http://stackoverflow.com/questions/1996184/all-possible-combination-for-an-hex-value-from-a-given-set-of-chars)
[https://www.offensive-security.com/metasploit-unleashed/generating-payloads/](https://www.offensive-security.com/metasploit-unleashed/generating-payloads/)
[http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
[http://www.gnucitizen.org/blog/reverse-shell-with-bash/](http://www.gnucitizen.org/blog/reverse-shell-with-bash/)
[https://www.youtube.com/watch?v=v1OXNP_bl8U](https://www.youtube.com/watch?v=v1OXNP_bl8U)
[https://community.rapid7.com/thread/2082](https://community.rapid7.com/thread/2082)
[https://www.phillips321.co.uk/2012/02/05/reverse-shell-cheat-sheet/](https://www.phillips321.co.uk/2012/02/05/reverse-shell-cheat-sheet/)
[http://offset-db.com/](http://offset-db.com/)

Specific Exploits

[http://www.carnal0wnage.com/papers/LARES-ColdFusion.pdf](http://www.carnal0wnage.com/papers/LARES-ColdFusion.pdf)
[http://web.archive.org/web/20141004091538/http:/www.slaughterjames.com/blog/2012/10/23/hacking-a-domain-controller-part-1-enumeration.html](http://web.archive.org/web/20141004091538/http:/www.slaughterjames.com/blog/2012/10/23/hacking-a-domain-controller-part-1-enumeration.html)
[https://adsecurity.org/?p=556](https://adsecurity.org/?p=556)
[https://www.offensive-security.com/metasploit-unleashed/client-side-exploits/](https://www.offensive-security.com/metasploit-unleashed/client-side-exploits/)
[https://www.tutorialspoint.com/cprogramming/c_pointers.htm](https://www.tutorialspoint.com/cprogramming/c_pointers.htm)

Networking

[http://alumni.cs.ucr.edu/~marios/ethereal-tcpdump.pdf](http://alumni.cs.ucr.edu/~marios/ethereal-tcpdump.pdf)
[https://danielmiessler.com/study/tcpdump/](https://danielmiessler.com/study/tcpdump/)
[https://openvz.org/Traffic_accounting_with_iptables](https://openvz.org/Traffic_accounting_with_iptables)
[https://technet.microsoft.com/en-us/library/cc771920(v=ws.10).aspx](https://technet.microsoft.com/en-us/library/cc771920(v=ws.10).aspx)

Misc

[https://www.exploit-db.com/docs/172.pdf](https://www.exploit-db.com/docs/172.pdf)
[http://www.advancedpentest.com/help-beacon-peer](http://www.advancedpentest.com/help-beacon-peer)
[http://blog.cobaltstrike.com/2013/12/06/stealthy-peer-to-peer-cc-over-smb-pipes/](http://blog.cobaltstrike.com/2013/12/06/stealthy-peer-to-peer-cc-over-smb-pipes/)
[https://github.com/samratashok/nishang/tree/master/Escalation](https://github.com/samratashok/nishang/tree/master/Escalation)
[http://www.powershellempire.com/](http://www.powershellempire.com/)
[https://jivoi.github.io/2015/07/01/pentest-tips-and-tricks/](https://jivoi.github.io/2015/07/01/pentest-tips-and-tricks/)
[https://github.com/g0tmi1k/](https://github.com/g0tmi1k/)
[https://highon.coffee/blog/penetration-testing-tools-cheat-sheet/](https://highon.coffee/blog/penetration-testing-tools-cheat-sheet/)

Metasploit

[https://github.com/g0tmi1k/mpc](https://github.com/g0tmi1k/mpc)
[http://netsec.ws/?p=262](http://netsec.ws/?p=262)
[https://www.offensive-security.com/metasploit-unleashed/msfconsole-commands/](https://www.offensive-security.com/metasploit-unleashed/msfconsole-commands/)
[https://www.offensive-security.com/metasploit-unleashed/msfcli/](https://www.offensive-security.com/metasploit-unleashed/msfcli/)
[https://www.sans.org/security-resources/sec560/misc_tools_sheet_v1.pdf](https://www.sans.org/security-resources/sec560/misc_tools_sheet_v1.pdf)
[https://www.offensive-security.com/metasploit-unleashed/writing-meterpreter-scripts/](https://www.offensive-security.com/metasploit-unleashed/writing-meterpreter-scripts/)

Recon

[http://www.sersc.org/journals/JSE/vol5_no5_2008/6.pdf](http://www.sersc.org/journals/JSE/vol5_no5_2008/6.pdf)
[http://www.pentest-standard.org/index.php/Intelligence_Gathering](http://www.pentest-standard.org/index.php/Intelligence_Gathering)
[http://bencane.com/2013/02/25/10-nmap-commands-every-sysadmin-should-know/](http://bencane.com/2013/02/25/10-nmap-commands-every-sysadmin-should-know/)
[http://resources.infosecinstitute.com/nmap-cheat-sheet-discovery-exploits-part-2-advance-port-scanning-nmap-custom-idle-scan/](http://resources.infosecinstitute.com/nmap-cheat-sheet-discovery-exploits-part-2-advance-port-scanning-nmap-custom-idle-scan/)
[https://media.blackhat.com/bh-us-11/Arsenal/BH_US_11_Nitrous_DotDotPwn_Slides.pdf](https://media.blackhat.com/bh-us-11/Arsenal/BH_US_11_Nitrous_DotDotPwn_Slides.pdf)
[https://support.microsoft.com/en-us/kb/142982](https://support.microsoft.com/en-us/kb/142982)
[http://security.stackexchange.com/questions/110673/how-to-find-windows-version-from-the-file-on-a-remote-system](http://security.stackexchange.com/questions/110673/how-to-find-windows-version-from-the-file-on-a-remote-system)
[http://carnal0wnage.attackresearch.com/2007/07/enumerating-user-accounts-on-linux-and.html](http://carnal0wnage.attackresearch.com/2007/07/enumerating-user-accounts-on-linux-and.html)
[https://scottlinux.com/2012/07/12/create-html-reports-with-nikto-web-server-scanner/](https://scottlinux.com/2012/07/12/create-html-reports-with-nikto-web-server-scanner/)
[https://curl.haxx.se/docs/httpscripting.html](https://curl.haxx.se/docs/httpscripting.html)
[http://resources.infosecinstitute.com/nmap-cheat-sheet-5-the-final-view-of-a-ninja-pentester/](http://resources.infosecinstitute.com/nmap-cheat-sheet-5-the-final-view-of-a-ninja-pentester/)
[https://www.digitalocean.com/community/tutorials/how-to-use-netcat-to-establish-and-test-tcp-and-udp-connections-on-a-vps](https://www.digitalocean.com/community/tutorials/how-to-use-netcat-to-establish-and-test-tcp-and-udp-connections-on-a-vps)
[http://www.securitysift.com/offsec-pwb-oscp/](http://www.securitysift.com/offsec-pwb-oscp/)

## Conclusion

Ran out of time, will add soon

