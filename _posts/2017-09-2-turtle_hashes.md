---
title:  "Stealing Hashes with LAN Turtle"
header: "Stealing Hashes with LAN Turtle"
categories: 
  - tutorial
tags:
  - lanturtle
  - hashes
---
When you hear that you can steal user hashes from locked machines, everyone’s ears perk up. This attack vector has been around for almost a year now, which surprised me that several pen testers/security experts were either totally unaware or not utilizing it in their physical penetration exercises. Below I’ll try my hand at explaining the attack as well as my experience with conducting it.  

{% include toc title="Table of Contents" icon="file-text" %}

# Attack  
***

Essentially you can configure and plug in a Hak5 LAN Turtle into a locked (logged in but locked) machine and it will store user hashes onto the Turtle within a matter of seconds. It does this by winning out to be the “newest most fastest” network attached and responder spoofs several roles, thus allowing the authentication challenge to occur which has the hash within it.  

# History  
***

This attack appears to have been first published on [Mubix’s site](https://room362.com/post/2016/snagging-creds-from-locked-machines/) on Sep 6, 2016. He describes in great detail how to replicate this attack (even on a USB Armory) and why and how this attack works.

# Tools  
***

Only a [Hak5 LAN Turtle](https://hakshop.com/collections/lan-turtle/products/lan-turtle)

But it’s always nice to have options… If you have the extra money to fork over, then you can accomplish this with a [USB Armory](https://inversepath.com/usbarmory). I personally haven’t used it for this attack but have read of its success. There are some trade offs, it doesn’t look as inconspicuous as the Turtle but it does offer more development control.  

# Process  
***

### Overview  

This was my first time using the Turtle so I had to go through the setup process and download the various modules. I think it’s important to wade through the documentation and setup videos offered on their [wiki](https://lanturtle.com/wiki/#!index.md), so that you understand all the options/functionality that comes with it. The documentation is laid out well and it’s easy to follow, so don’t skip this step, go explore it. With that being said, I won’t offer instructions on the Turtle setup. However, we will go over the specifics to this attack.  

I recommend installing all the modules that are offered so that you can have them readily available anytime you want to play around with them. Once you have them, the Hak5 guys were nice enough to create a module for this exercise called “QuickCreds”.  

### Setup  

Log into the Turtle and select “Modules”

![Turtle Modules](/assets/images/turtle_mods.jpg)  

Select “QuickCreds”

![Turtle QuickCreds](/assets/images/turtle_quickcreds.jpg)  

Select “Enable”, so that it starts whenever the Turtle is plugged into the Target Machine

> Optional – If you didn’t download the module then you can click “Configure” and download it at that time.  
> Optional – If you want to test QuickCreds against your machine currently then you can start it by selecting “Start”  

### Capturing Credentials  

Insert the Turtle into a logged in but locked machine and wait for the credentials to be harvested. With the QuickCreds module, you can view the status of the operation by the light indicator. Once the light begins blinking rapidly, the credentials have been captured and you can simply remove the Turtle from the machine.  

To view the captured credentials, you can plug the Turtle back into your machine and connect to it via Putty. Go to the “Exit” option so that you’ll be presented with a command prompt, which you already know because you read the wiki (right?). Change to the loot directory with `cd loot` and display the files located within that folder with `ls -al`. You should see a responder.log and one or more folders that are numbered numerically. Each time you plug in the Turtle and it begins to capture credentials, it will store the results in a separate folder. To view the harvested credential simply open the respective folder and look for a text file containing the credentials (example: Proxy-Auth-NTLMv2-3.123.14.184.txt).  

![Turtle List](/assets/images/turtle_list.jpg)  

Within the file you should be presented with something similar to the below line  

```User1::domain1:52ca42bcd7ea58ee:12dcce4246268262a153b5064d58dac6:5c78dcs3153d840d1110
0000000000c45467103d4777bb5a2d12f1a11230c0000000062920b25fa8da13c31cdb3b72f5c715c713010```  

The User1 section is the username and the domain1 section is the domain in which the machine is located on. The following information is the hash that you would most likely throw into hashcat or use within your favorite cracking method.  

# My Experience  

Since Hak5 was kind enough to script this into a module, it made this exercise a snap. I’ve had mixed results on timing and the ability to pull the credentials though. From my research online, this seems to be a common theme and perhaps the inability for some machines to download/enable the correct driver. However, I would say that the majority of my tests passed with flying colors. I tried various OS’s and I didn’t particularly find any that it just didn’t work on. The light sequence used in QuickCreds sometimes was right and sometimes it wasn’t but for the most part it did well.  

# Take-A-Ways  

 - Combining this with other attack methods (the Turtle can offer a shell back to you!) offer a ton of options and attacking scenarios to conduct  
 - Since just about every OS is going to trust Ethernet/LAN and employees typically need a USB, it would difficult to find an enterprise level defense solution. Thusly, this is going to increase your chances at advancing your physical pen test.  
 - This is super simple to carry out and usually can be done within 30 seconds. The LAN Turtle disguises itself nicely which is certainly a perk for going for the cheaper option.  
 - Depending on the hash that you've obtained, you could attempt a pass-the-hash type attack and not even bother with cracking

# Great Resource  

[Snagging Creds From Locked Machines With a LAN turtle - Hak5 2104](https://www.youtube.com/watch?v=AVqh5mcFcFU)  
