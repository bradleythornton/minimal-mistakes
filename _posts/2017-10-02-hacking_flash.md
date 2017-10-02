---
title:  "Hacking Flash Games (Client-side Attack)"
header: "Hacking Flash Games (Client-side Attack)"
categories: 
  - tutorial
tags:
  - flash
---

One of the areas of interest that first led to me to becoming passionate about security was the Game Genies and Game Sharks. I thought it was fascinating to find these little nuggets that allowed me to interact with the game in a way that the developers didn’t intend for me to. In some instances, finding the cheat codes or hacks were more interesting than the game itself. So, while I was playing a couple of flash games and came across an article at [Privsec](https://privsec.blog/penetration-testing-flash-apps-aka-how-to-cheat-at-blackjack/). I got the bug again and this post is the outcome of that. Hopefully this intrigues you to test applications that your company uses that may be vulnerable to a client-side attack (with permission of course). My examples below are innocent in nature but there are some very real-world scenarios that aren’t.  

> **Disclaimer:** This along with all other information found on my blog is for educational purposes only. Please don’t use this information to earn badges, be placed on leaderboards, cheat for monetary gain, or commit any illegal activities. Not only in most cases is it against terms of use but in some situations, it is blatantly illegal.  

# Tools  
***

- [Cheat Engine](http://www.cheatengine.org/)
- [Burp](https://portswigger.net/burp)
- [JPEXS Free Flash Decompiler - FFDec](https://www.free-decompiler.com/flash/download/)
- Flash game of your choosing

# Process  
***

**Option 1 - Memory**  
- Download Cheat Engine
- Attach Cheat Engine to process
- Find memory location
- Modify memory location value


**Option 2 - Static Code**  
- Obtain SWF file
- Load SWF file in Decompiler
- Modify SWF file
- Verify Changes
- Optional: Replay in session

# Option 1 - Memory  
***

I would be remiss if I didn’t at least mention Cheat Engine in an article about modifying games. There’s a plethora of tutorials on how to operate and use Cheat Engine so I won’t belabor that any more than it already has. I’ve had varying degrees of success with it but overall, I think it’s an impressive tool to have in your arsenal. You can download it [here](http://www.cheatengine.org/downloads.php) and find tutorials and cheat tables [here](http://forum.cheatengine.org/viewforum.php?f=7) and [here](http://fearlessrevolution.com/). I’ll provide some highlights just so you know where this fits into the whole grand scheme of this post and to not make it too lengthy. Instead of decompiling the application and making modifications, you may be able to alter the application on the fly within memory. This is a quick way of modifying games and may prove to be fruitful when you’re in a rush. Essentially you download Cheat Engine, attach it to the games process, find the memory location of the value you want to change, and change it. Since this was all a learning experience for me, I can’t vouch as to the reliability of this but in my case I was able to easily do it with some games and not so much with others. However, the decompiling option I’ve been very successful with thus far.  

# Option 2 - Decompiling  
***

## Obtain SWF file  
***

First, we’ll need to obtain the SWF file for tampering. You can do this in various ways such as navigating directly to the flash game file, pulling it from your browsers cache, or using a web proxy to find its location if you are unable to naturally. In this example, we’ll use Burp as our web proxy to identify the SWF file. Configure your browser to run through Burp, detailed instructions can be found [here](https://support.portswigger.net/customer/portal/articles/1783055-configuring-your-browser-to-work-with-burp). You should clear your browsers cache to ensure that the file will be downloaded. Navigate to the game with interceptor turned on. You’ll likely have to forward several requests due to ads and things of that nature but what you’re ultimately looking for is a GET request for a SWF file. Your request would look something like the below example.   

![Burp Interception](/assets/images/flashburp1.jpg)  

With this you have two options:  
Go to “Response” > “Headers” tab and will see various strange characters, simply right-click and choose “Copy to file” and name it whatever you’d like plus “.swf”  

![Burp Response Header](/assets/images/flashburp2.jpg)  

Or you can simply navigate directly to the swf file (location is highlighted in green) and you can do a “File” > “Save As”  

> Side-Note: If you happen to skip the request and need to come back you can always review previous requests in the HTTP History tab.  

## Load SWF file in Decompiler  
***

When installing FFDec, make sure that you include the “Download PlayerGlobal.swc” as this will be needed; the other items are at your discretion.  

![FFDec Installation](/assets/images/flashffdecinstall.jpg)  

Open FFDec and within it open the SWF file that you saved earlier. This next process will vary dependent upon the flash game that you are attempting to manipulate and what exactly you’re trying to accomplish. For the sake of example, we’ll attempt at modifying the amount of cash that we start with in the game. In my experience, the most interesting information can be found in the “scripts” directory which can be expanded upon in the far-left pane.  

![FFDec Game Directory](/assets/images/flashgamefolder.jpg)  

I typically search through the various parameters and files located within that directory until I find something interesting. In this case I’m looking for a variable called money/cash/coin or something of that nature. The screenshot below shows an example of what you may find within the game (line 4).  

![Game 1 Example](/assets/images/flashexample1.jpg)  

However, some applications have these variables buried within additional code that doesn’t quite stick out so blatantly (see line 370)  

![Game 2 Example](/assets/images/flashexample2.jpg)  

> Side-note: If you start the game off with a certain amount of cash then you can search for that value as well. If you can’t locate the variable that you are looking for then you could attempt at altering other variables that will have a similar effect, such as reducing the cost of everything to free or magnifying loot drops for additional resources.  

## Modify SWF file  
***

To modify the desired value, click the “Edit ActionScript” button in the center pane. Make the necessary modification and click “Save” at the bottom. Once all modifications have taken place be sure to click “Save” in the upper toolbar as well.  

![Edit Action Script](/assets/images/flasheditaction.jpg)  
![FFDec Save](/assets/images/flashsave.jpg)  

If you find multiple variables and are unsure of which will have the desired result, then it’s wise to test each one individually. If you choose to change multiple variables at one time, to keep them separated I typically use a unique string to make it easier to identify. An example would be, change variable1 to “88888” and variable2 to “99999”. If you find your desired result equals “99999” then you know that variable2 is what you’ll want to modify.  

## Verify Changes  
***

Before loading the game, delete your browsers cache or use a private browsing option such as Incognito mode for Chrome or InPrivate browsing for Internet Explorer. Depending on the games flow and the variable that was modified you may receive money after a splash screen, a certain action has been completed, or simply at the start. Understanding the flow of the game can open up a lot of opportunities to dictate how the application behaves so if you are struggling then I would recommend spending your time there.  

In this example, the first level must be completed before you have access to your cash  

![Results 1](/assets/images/flashresults1.jpg)  

In this example, you immediately are presented with your cash
  
![Results 2](/assets/images/flashresults2.jpg)  

> Side-Note: If you experience errors then you may have a number that’s too large and should reduce it to fit within the constraints of the application, or remove them completely if you are able to do so.  

## Optional: Replaying within the session  
***

If replaying within the session is the ultimately goal (remember, don’t do this to fulfill badges/leaderboard…just don’t be one of “those” people…) then we’ll return to Burp. You’ll need to restart your browser and clear the cache. Be on the lookout for the same request that you used to retrieve the SWF file. Right click in the white space and select “Do intercept” > “Response to this request”  

![Modify Burp Response](/assets/images/flashresponse1.jpg)  

Forward the requests until you see a “Response from http://<SITE YOU ARE EXPECTING>”. On the “Headers” tab, scroll to the bottom where you see the random characters and delete everything located there. Right-click and select “Paste from file” in which you load up the SWF file that you modified and press “Forward”. At this point you can turn intercept off and enjoy the game within the browser.  

![Send Modified Burp Response](/assets/images/flashresponse2.jpg)  
