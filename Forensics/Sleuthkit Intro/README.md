# Sleuthkit Intro
## Author
LT 'syreal' Jones
## Description
Download the disk image and use `mmls` on it to find the size of the Linux partition. Connect to the remote checker service to check your answer and get the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
* [Download disk image](https://artifacts.picoctf.net/c/114/disk.img.gz)
* Access checker program: `nc saturn.picoctf.net 52279`
## Approach
A [gzip](https://www.gnu.org/software/gzip/) file is compressed data, it's similar to a zip file. There's smomething inside the gzip so we can take a look. Open the gizp using [7zip](https://www.7-zip.org/) then extract the file (there are other methods using terminal but 7zip is easy to do).  
Extract `disk.img`. We can read the hint and do literally that.
```
$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000204799   0000202752   Linux (0x83)
```
Great! Now we know the size of the Linux partition is 202752 (length of the 2nd partition) we can connect to the shell and get our flag.
```
$ nc saturn.picoctf.net 52279
What is the size of the Linux partition in the given disk image?
Length in sectors: 202752
202752
Great work!
picoCTF{mm15_f7w!}
```
## Flag
picoCTF{mm15_f7w!}