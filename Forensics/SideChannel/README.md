# SideChannel
## Author
Anish Singhani
## Description
There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?  
Download the PIN checker program here [`pin_checker`](./pin_checker)  
Once you've figured out the PIN (and gotten the checker program to accept it), connect to the master server using `nc saturn.picoctf.net 53639` and provide it the PIN to get your flag.
## Hints
1. Read about "timing-based side-channel attacks."
2. Attempting to reverse-engineer or exploit the binary won't help you, you can figure out the PIN just by interacting with it and measuring certain properties about it.
3. Don't run your attacks against the master server, it is secured against them. The PIN code you get from the `pin_checker` binary is the same as the one for the master server.
## Approach
### Understanding Timing Based Side Channel Attacks
After looking at hint number one and skimming through the [Wikipedia page](https://en.wikipedia.org/wiki/Timing_attack), I learned timing attacks use how long it takes for a program to run to figure out how close they are to obtaining actual credentials. The reasoning behind this is a program will go through a series of checks and if one check checks false, the program breaks. The longer it takes for the program to check, the closer you are to obtaining a legit credential. Using this, we can conclude that the longer it takes for the checker to execute, the closer we are to the correct pin.
### The Code
My first iteration of the script looked like this:
```python
import os
import time

n = input()
s = time.time()
os.system(f"echo {n} | ./pin_checker")
print(time.time() - s)
```
That didn't work. The problem with this was that the operating system is always going to be running background tasks which will create slight variances and those varaiances screw up individual results. I arbitrarily chose 100 as a sample size because I figured (guessed) that wouldn't take forever to run and wouldn't have too much variation. The result is [here](./script.py)
### Solving
I ran `python3 script.py` and inputted values. At first I thought it would be checking by bits so I checked against binary numbers but at some point, realized that wasn't the case. After that, I wrote down the digits possible digits followed by padding zeroes. Whichever value took the longest runtime would be the most correct one. All data is messily recorded in [`data.txt`](./data.txt).
### Getting the Flag
Eventually, `48390513` worked for the pin:
```
$ ./pin_checker
Please enter your 8-digit PIN code:
48390513
8
Checking PIN...
Access granted. You may use your PIN to log into the master server.
```
Now we can connect with `nc saturn.picoctf.net 53639` and input the pin:
```
$ nc saturn.picoctf.net 53639
Verifying that you are a human...
Please enter the master PIN code:
48390513
Password correct. Here's your flag:
picoCTF{t1m1ng_4tt4ck_0431e830}
```
## Flag
picoCTF{t1m1ng_4tt4ck_0431e830}