# Operation Orchid
## Author
LT 'syreal' Jones
## Description
Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
* [Download compressed disk image](https://artifacts.picoctf.net/c/240/disk.flag.img.gz)
## Approach
First let's download and extract the file with `gzip -d disk.flag.img.gz`. We should now take a look at the partitian contents:
```
$ mmls disk.flag.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000411647   0000204800   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000411648   0000819199   0000407552   Linux (0x83)
```
The first few partitians don't have anything interesting. The last partitian shows this:
```
$ fls -o 411648 disk.flag.img
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 81: proc
d/d 82: dev
d/d 83: tmp
d/d 84: lib
d/d 87: var
d/d 96: usr
d/d 106:        bin
d/d 120:        sbin
d/d 460:        home
d/d 466:        media
d/d 470:        mnt
d/d 471:        opt
d/d 472:        root
d/d 473:        run
d/d 475:        srv
d/d 476:        sys
d/d 2041:       swap
V/V 51001:      $OrphanFiles
```
Once again, we will start our search in the `root` directory:
```
$ fls -o 411648 disk.flag.img 472
r/r 1875:       .ash_history
r/r * 1876(realloc):    flag.txt
r/r 1782:       flag.txt.enc
```
Unfortunately, `flag.txt` doesn't seem to hold anything interesting and `flag.txt.enc` seems to be gibberish:
```
$ icat -o 411648 disk.flag.img 1876
           -0.881573            34.311733
```
A quick search will show that [`.ash_history`](https://vconnectit.wordpress.com/tag/ash_history/) is a file where past commands are stored so let's take a look at that:
```
$ icat -o 411648 disk.flag.img 1875
touch flag.txt
nano flag.txt
apk get nano
apk --help
apk add nano
nano flag.txt
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
```
Looking at this, we now know what the user did:
1. create a `flag.txt` file
2. attempt to edit the `flag.txt` file then realize they don't have [`nano`](https://www.nano-editor.org/)
3. attempt to install `nano`
4. look for help on how to use [`apk`](https://wiki.alpinelinux.org/wiki/Package_management)
5. finally install `nano`
6. use `nano` to edit `flag.txt`
7. check out [`openssl`](https://www.openssl.org/)
8. use `openssl` to encrypto `flag.txt` using aes256 with "unbreakablepassword1234567" as the password and `flag.txt.enc` as the output file
9. destroy `flag.txt` so the contents are overwritten with useless stuff
10. check the permissions of everything in the directory
11. stop all CPU functions
Knowing this, we now know we just need to decrypt `flag.txt.enc` with `openssl`. We can start by copying the `flag.txt.enc` file to our local device: `icat -o 411648 disk.flag.img 1782 > flag.txt.enc` and now we can decrypt the file:
```
$ openssl aes256 -d -in flag.txt.enc -out flag.txt
enter aes-256-cbc decryption password:
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
140612745892480:error:06065064:digital envelope routines:EVP_DecryptFinal_ex:bad decrypt:../crypto/evp/evp_enc.c:583:
```
I also love errors but hey, it got us the flag:
```
$ cat flag.txt
picoCTF{h4un71ng_p457_17237fce}
```
## Flag
picoCTF{h4un71ng_p457_17237fce}