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
 - **Do VulnHub images!** Seriously, if you haven’t already then stop reading all the reviews and do some now before you even think about signing up. If you enjoy going through them then you’ll enjoy doing OSCP. It’s basically a free taste of it before you buy.

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
 - Don’t get stuck on any one machine rotate, every 3-4 hours
 - Write your report ahead of time so that you only need to add your exam notes in
 - Stick to your methodology and enumerate EVERYTHING
 - Start off with light port scans and work your way to more advanced ones
 - I had better luck with the higher point machines so I always started with those
 - Take a break of it all for a day or two before your exam

## Resources

Ran out of time, will add soon

## Conclusion

Ran out of time, will add soon

