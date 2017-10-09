---
title:  "TTY Spawning Cheat Sheet"
header: "TTY Spawning Cheat Sheet"
categories: 
  - cheatsheet
  - OSCP
tags:
  - tty
---

Below are some helpful tricks to spawn a TTY shell in the event you need to further interact with the system. These are also helpful in breaking out of "jail shells" but I'll attempt to cover more on that later

`python -c 'import pty; pty.spawn("/bin/sh")'`  
`echo os.system('/bin/bash')`  
`/bin/sh -i`  
`perl —e 'exec "/bin/sh";'`  
`perl: exec "/bin/sh";`  
`ruby: exec "/bin/sh"`  
`lua: os.execute('/bin/sh')`  
When in vi `:!bash` or `:set shell=/bin/bash:shell`  
When in nmap `!sh`  
