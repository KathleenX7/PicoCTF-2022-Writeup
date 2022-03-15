# Lookey here
## Author
LT 'syreal' Jones / Mubarak Mikail
## Hints
Download the file and search for the flag based on the known prefix.
## Description
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it.  
Download the data [here](./anthem.flag.txt).
## Approach
The hint is very good. We can follow the hint and use the command `cat anthem.flag.txt | grep pico` which will print out all lines in the file that has "pico" in it. That gives the output we think that the men of picoCTF{gr3p_15_@w3s0m3_429334b2}"
## Flag
picoCTF{gr3p_15_@w3s0m3_429334b2}