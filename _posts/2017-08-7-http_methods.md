---
title:  "Obtaining HTTP Request Method’s"
header: "Obtaining HTTP Request Method’s"
categories: 
  - tutorial
tags:
  - scanning
---

When conducting security reviews (penetration tests, vulnerability assessments, etc) understanding what HTTP request methods exists can become imperative to the risk score of your assets. I’ve found that this lesson can be garnered in numerous CTF’s that I’ve participated in. However, I’ve heard recent twitter discussions regarding exactly how to review the request methods so I figured it warranted a post. This of course is not an exhaustive list but it should point you in the right direction. Comment below if you want to share additional ways!  

These options aren’t full proof and it really depends on how the server is configured. The best method seems to be to test each method individually and inspect the results which I would recommend doing via Burp. 

## Curl  

I typically use curl as it’s just really quick and easy to do.  

![Curl Example](/assets/images/httpmethodcurl.jpg)  

## Nitko  

Nikto natively checks the HTTP methods for you and returns them. It’s good to keep in mind that different directories can have different methods though, so don’t just try the main directory.  

![Nikto Example](/assets/images/httpmethodnikto.jpg)  

## Metasploit  

There’s a built in scanner that will perform this check for you within Metasploit. This is a really nice way if you have multiple hosts you’d liked to scan.  

![Metasploit Example](/assets/images/httpmethodmeta.jpg)  

## Netcat  

You can do pretty much everything with Netcat, checking methods is no different  

![Netcat Example](/assets/images/httpmethodnetcat.jpg)  

## Nmap  

Nmap has a script that will send an OPTIONS request to the target server and return the methods. Be sure to check out some of the arguments as you can glean some extra information from those if necessary.  

![Nmap Example](/assets/images/httpmethodnmap.jpg)  

Hope this helps and be sure to post comments of any other options that you like.