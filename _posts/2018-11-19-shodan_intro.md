---
title:  "Intro to Shodan"
header: "Intro to Shodan"
categories: 
  - shodan
tags:
  - shodan
---

Shodan gets a bad rap. Many of you have probably heard the connotation that Shodan is “the world’s most dangerous search engine” or “dark Google” and it’s somehow only used by hackers to wreak havoc on IoT. While I can’t say it doesn’t make a malicious person’s aim at causing chaos easier, it’s also a great tool in a penetration testers arsenal. While explaining findings to a client it really helps to put things in perspective by showcasing how often it exists in the wild. By pointing out a massive misconfiguration and giving concrete evidence that it’s only done by 3 other places in the world, they start to get the picture. However, it doesn’t only assist in post exploitation endeavors, the passive recognizance is perhaps the most enticing part. I won’t harp on the value of OSINT and its importance in red teaming, but Shodan is a great addition and I’ve had a blast playing around with it.  

# What is it?  
***

You can take a look at what the Shodan Help Center has to say about it [here](https://help.shodan.io/the-basics/what-is-shodan). But in short, it’s a search engine for Internet-connected devices. Scanners identify listening ports and attempt to enumerate information from them. It typically collects this information from banners and query responses. This means it collects data from devices ranging from refrigerators to stop lights to SCADA systems. The best part is Shodan takes all this data and makes it easily searchable and categorized for you.  

# Interaction options  
***

You have a few different options to interact with Shodan from the web interface, API through command line tools, and there are even some Metasploit modules.  

# Create an account  
***

I’m going to assume you know how to create an account on a website and not waste your time. I do recommend the paid subscription as there are many benefits. One reason for the timing of this post was so that you can take advantage of their usual Black Friday deal which drastically reduces the cost of a lifetime membership from $50 to only $5. We can all agree that we have spent a lot more and received a lot less, so give it a shot.

# How to search  
***

![How to Shodan Search](/assets/images/shodan_search.jpg)  

As with most websites, you search in the white search bar at the top (depicted above is a search of IIS). You can find a quick cheat sheet for basic search filters as well as some examples [here](https://thor-sec.com/cheatsheet/shodan/shodan_cheat_sheet/). Once you’ve made a search you’ll receive the output. On the left are quick filters you can apply which will perform a new search with a stricter criteria and on the right you’ll get the result details in the format below:  

![image-right](/assets/images/shodan_entry.jpg){: .align-right}

- IP address
- Host name
- ISP
- Entry added to database
- Country
- Banner cataloged

A section that many fail to notice is the small “Details” link which really helps to profile a device. The details page lists out basic information, GPS map, ports, services, and even vulnerabilities. If you’re on an engagement, you’re already one step ahead and you haven’t even touched their network yet.  

![Detailed Shodan Result](/assets/images/shodan_detailed.jpg)  

Towards the top of the page, there’s a “View Raw Data” link that will provide you the value of each database property. This page is extremely useful when creating search criterias to find like devices.  
 
![Raw Data Shodan Result](/assets/images/shodan_raw_data.jpg)  

# Examples  
***
- Traffic lights
- Routers
- Webcams
- SCADA System

# Points of interest  
***

[Shodan Explore](https://www.shodan.io/explore) is a great starting point to demonstrate some of the juicy things that you can find on Shodan. This page allows you view search queries that other users have shared. I recommend making it one of your first stops, so you can get a feel for what data exists and how others have formed their search queries.
Combining data for fun and profit.  

[Shodan Exposure - Internet Exposure Observatory](https://exposure.shodan.io/#/)
Yet another Shodan feature that many may not be aware of, Shodan Exposure (Internet Exposure Observatory). This is a great tool to check country exposures and very interesting stats.  

![Shodan Exposure - US](/assets/images/shodan_exposure.jpg)  
 
[Shodan Images](https://images.shodan.io/)
And yet another Shodan feature that many may not be aware of, Shodan Images. This one is self-explanatory but extremely interesting. It grabs screenshots of various devices such as desktops and webcams.  

[Retro Shodan](https://2000.shodan.io/#/)
This is more for fun than anything else, but a new theme was released as an 80’s retro version of Shodan. By the way, it comes with music so enable it at the top!

![Shodan 2000](/assets/images/shodan_2000.jpg)  

[Ship Tracker](https://shiptracker.shodan.io/)
Well known Ship Tracker that was discussed at Defcon one year by Jeff Merrick. Not sure if it’s still used/updated but it tracks ships by correlating AIS GPS coordinates and satcom box profiles on Shodan.  

[Shodan Exploits](https://exploits.shodan.io)
Another Shodan feature that many may not be aware of, Shodan Exploits. It works similar to the rest of the tool suite but it’s a great way to search for exploits across a multitude of resources. See example below of a CISCO ASA 8 search.  

![Shodan Exploit Result](/assets/images/shodan_exploit.jpg)  
 
[Here’s](https://thor-sec.com/cheatsheet/shodan/shodan_cheat_sheet/) a quick rundown of Shodan Exploit search filters.  

[Interactive Camera Map](https://github.com/woj-ciech/kamerka)
Tool to help with creating maps with cameras based on geolocation and Shodan. This is a great OSINT tool, particularly in relation to physical assessments.  

[SearchDiggity](https://www.bishopfox.com/resources/tools/google-hacking-diggity/attack-tools/)
This tool didn’t really fit anywhere else, but it definitely warrants mention. Bishop Fox added an additional tool “SHODAN Diggity” which makes for an easy interface to Shodan and a great way to look at a particular targets Internet footprint.  

[Real-Time Network Monitoring](https://help.shodan.io/guides/how-to-monitor-network)
There’s already a great writeup on how to do this at the link but I thought this was an interesting way to set up network alerts by using Shodan.  

[AutoSploit](https://github.com/NullArray/AutoSploit)
I was reluctant to provide a link to this tool as I have mixed feelings about it’s existence and don’t want to spread it around anymore than it already has been. However, it grabs hosts from Shodan and runs Metasploit modules against them. It essentially takes all the fun out of hacking and is a “click, click, bacon” type of tool. There are certainly opportunities where this can be helpful to an organization, but in reality, it isn’t primarily used that way. It’s an interesting idea and neat to play around with, just don’t be one of “those people” if you can help it.  

# Legal issues  
***
I would be remiss if I at least didn’t mention that many countries have different laws on what constitutes hacking or misuse of a computer system. In some countries merely attempting default credentials on a device you don’t own is considered “hacking” and punishable by law. Act responsibly…or whatever phrase helps deter you from going over to the dark side.  

# Shodan API  
***
There’s some great documentation on how to use the Shodan API and I plan to create a blog post solely focusing on it. In the meantime, check out the [official documentation](https://developer.shodan.io/api/clients) to get started.  

# Shodan in Metasploit  
***
There are two modules included with Metasploit.  
auxiliary/gather/shodan_search – This module uses the Shodan API to search Shodan. You’ll need to include your Shodan API Key to complete searches, particularly if you have the paid subscription. Set the values as you would in any other Metasploit module by placing your values in each parameter. A handy tool is the outfile parameter which allows you to export your results. The example below is of a quick IIS search.  
![Metasploit Shodan Search Module](/assets/images/shodan_metasploit1.jpg)   

auxiliary/gather/shodan_honeyscore – This module uses the Shodan API to check if a server is a honeypot or not. It’ll return a score from 0.0 to 1.0, the larger the number the more likely it is a honeypot. Same rules apply as the previous module in that you need to utilize a Shodan API Key. Alternatively, you can do this from the web interface by going to https://honeyscore.shodan.io/.   
![Metasploit Shodan Honeypot Search Module](/assets/images/shodan_honeypot.jpg)  

# Additional References  
***
- Complete guide to shodan - https://leanpub.com/shodan
- Follow them on twitter for updates, new features, and tool references https://twitter.com/shodanhq?lang=en
- Check out some of the other tools that are offered through Shodan https://www.shodan.io/about/products
