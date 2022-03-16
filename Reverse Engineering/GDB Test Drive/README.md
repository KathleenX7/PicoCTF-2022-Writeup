# GDB Test Drive
## Author
LT 'syreal' Jones
## Description
Can you get the flag?  
Download this [`binary`](./gdbme).  
Here's the test drive instructions:
* `$ chmod +x gdbme`
* `$ gdb gdbme`
* `(gdb) layout asm`
* `(gdb) break *(main+99)`
* `(gdb) run`
* `(gdb) jump *(main+104)`
## Approach
Follow the commands in the description:
```
$ gdb gdbme
GNU gdb (Ubuntu 9.2-0ubuntu1~20.04) 9.2
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from gdbme...
(No debugging symbols found in gdbme)
(gdb) layour asm
Undefined command: "layour".  Try "help".
(gdb) break *(main+99)
Breakpoint 1 at 0x132a
(gdb) run
Starting program: /mnt/c/Users/Vivian/downloads/gdbme

Breakpoint 1, 0x000000000800132a in main ()
(gdb) jump *(main+104)
Continuing at 0x800132f.
picoCTF{d3bugg3r_dr1v3_93b87433}
[Inferior 1 (process 267) exited normally]
(gdb) quit
```
## Flag
picoCTF{d3bugg3r_dr1v3_93b87433}