---
title:  "Shodan Cheat Sheet"
header: "Shodan Cheat Sheet"
categories: 
  - Cheatsheet
  - Shodan
tags:
  - Shodan
---

Shodan's a search engine which helps find systems on the internet. It's a great resource to provide passive reconnaissance on a target or as a measuring tool for how widespread a configuration or device is.

![Shodan Banner](/assets/images/shodan_banner.jpg)  

# Basic Search Filters  
***
<strong>port:</strong> `Search by specific port`  
<strong>net:</strong> `Search based on an IP/CIDR`  
<strong>hostname:</strong> `Locate devices by hostname`  
<strong>os:</strong> `Search by Operating System`  
<strong>city:</strong> `Locate devices by city`  
<strong>country:</strong> `Locate devices by country`  
<strong>geo:</strong> `Locate devices by coordinates`  
<strong>org:</strong> `Search by organization`  
<strong>before/after:</strong> `Timeframe delimiter`  
<strong>hash:</strong> `Search based on banner hash`  
<strong>has_screenshot:true</strong> `Filter search based on a screenshot being present`  
<strong>title:</strong> `Search based on text within the title`  
  

# Examples
***
Webcamxp instances in the US  
`webcamxp country:"US"`  

Cisco devices in New York  
`cisco city:"New York"`  

Unsecured Linksys Webcams with screenshots in the search query  
`title:"+tm01+" has_Screenshot:true`  

# Additional filters through REST and Streaming API
***
[Shodan Developer - Banner Specification](https://developer.shodan.io/api/banner-specification)  
