# File types
## Author
Geoffrey Njogu
## Description
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.  
You can download the file from [here](./Flag.pdf).
## Hints
1. Remember that some file types can contain and nest other files
## Approach
This was a very tedious question. Let's start by checking what type of file the PDF file actually is:
```
$ file flag.pdf
flag.pdf: shell archive text
```
Now that we know it's a [`shar` file](https://en.wikipedia.org/wiki/Shar) we can rename it to `flag.shar` with `mv flag.pdf flag.shar`. I took a look at [this article](https://www.maketecheasier.com/create-self-extracting-archives-shar-linux/) to see how to extract a shar file:
```
$ ./flag.shar
x - created lock directory _sh00047.
x - extracting flag (text)
x - removed lock directory _sh00047.
```
Now we have another flag file so we'll need to repetitively check what type of file it is and rename it:
```
$ file flag
flag: current ar archive
$ mv flag flag.a
```
Any time the file is renamed, extension is coming from [Wikipedia](https://en.wikipedia.org/wiki/Ar_(Unix)). [This article](https://www.geeksforgeeks.org/ar-command-in-linux-with-examples/) explained how to extract an ar file:
```
$ ar xv flag.a
x - flag
```
I took a look at [this article](https://www.thegeekstuff.com/2010/08/cpio-utility/):
```
$ file flag
flag: cpio archive
$ mv flag flag.cpio
$ cpio -idv < flag.cpio
flag
2 blocks
```
As you can see, this process is pretty repetitive, next let's look at [this article](https://www.tecmint.com/linux-compress-decompress-bz2-files-using-bzip2/):
```
$ file flag
flag: bzip2 compressed data, block size = 900k
$ mv flag flag.bz2
$ bzip2 -d flag.bz2
```
[Again](https://help.nexcess.net/77285-other/how-to-decompress-files-in-gzip):
```
$ file flag
flag: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:46 2022, from Unix, original size modulo 2^32 330
$ mv flag flag.gz
$ gzip -d flag.gz
```
An alternative and more efficient method than searching for articles is using `man` pages or using the `--help` option then searching for "decompress" because this question is very repetitive.
```
$ file flag
flag: lzip compressed data, version: 1
$ mv flag flag.lz
$ lzip -d flag.lz
```
If you ever run into not having something, you can use [`brew`](https://brew.sh/) or [`apt`](https://wiki.debian.org/Apt) to install it.
```
$ file flag
flag: LZ4 compressed data (v1.4+)
$ mv flag flag.lz4
$ unlz4 flag.lz4
Decoding file flag
flag.lz4             : decoded 266 bytes
```
There's also [these pages](https://linux.die.net/man/1/lzma) 
```$ file flag
flag: LZMA compressed data, non-streamed, size 255
$ mv flag flag.lzma
$ lzma -d flag.lzma
```
Pretty sure basically everything after this was just `-d`:
```
$ file flag
flag: lzop compressed data - version 1.040, LZO1X-1, os: Unix
$ mv flag flag.lzop
$ lzop -d flag.lzop
```
Wow another lzip:
```
s$ file flag
flag: lzip compressed data, version: 1
$ mv flag flag.lz
$ lzip -d flag.lz
```
XZ is installed with `sudo apt-get install xz-utils`:
```
$ file flag
flag: XZ compressed data
$ mv flag flag.xz
$ unxz flag.xz
```
Now we stumble across something revolutionary! We come across an ASCII text file!:
```
$ file flag
flag: ASCII text
$ cat flag
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f35613833373565307d0a
```
The output looks like hex so we can use an [online hex decoder](http://www.unit-conversion.info/texttools/hexadecimal/) to get the flag.
## Flag
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_5a8375e0}