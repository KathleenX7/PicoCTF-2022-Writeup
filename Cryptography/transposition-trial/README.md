# transposition-trial
## Author
Will Hong
## Description
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.  
Download the corrupted message [here](./message.txt).
## Hint
1. Split the message up into blocks of 3 and see how the first block is scrambled
## Approach
We can do what the hint says. If we split the chunks of 3 by newline: 
```
heT
fl 
g a
s i
icp
CTo
{7F
4NR
P05
1N5
_16
_35
P3X
51N
3_V
CDE
4CE
4}7
```
We can then assume the first word is supposed to be "The". "heT" to "The" is taking the last character and moving it to the front. We then get "The flag is picoCT{F7R4N5P051N6_15_3XP3N51V3_ECDE4C74}"
## Flag
picoCTF{7R4N5P051N6_15_3XP3N51V3_ECDE4C74}