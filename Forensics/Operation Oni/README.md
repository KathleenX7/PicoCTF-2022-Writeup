# Operation Oni
## Author
LT 'syreal' Jones
## Description
Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.
* [Download disk image](https://artifacts.picoctf.net/c/374/disk.img.gz)
* Remote machine: `ssh -i key_file -p 58852 ctf-player@saturn.picoctf.net`
## Approach
First we extract the file with `gzip -d disk.img.gz`. We'll then take a look at the disk:
```
$ mmls disk.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000471039   0000264192   Linux (0x83)
```
The partitian on 2048 is the operating system which we don't care about. On 206848 we get the user's files:
```
$ fls -o 206848 disk.img
d/d 11: lost+found
d/d 12: boot
d/d 13: etc
d/d 79: proc
d/d 80: dev
d/d 81: tmp
d/d 82: lib
d/d 85: var
d/d 94: usr
d/d 104:        bin
d/d 118:        sbin
d/d 458:        home
d/d 464:        media
d/d 468:        mnt
d/d 469:        opt
d/d 470:        root
d/d 471:        run
d/d 473:        srv
d/d 474:        sys
V/V 33049:      $OrphanFiles
```
Once again, we should explore the `root` folder:
```
$ fls -o 206848 disk.img 470
r/r 2344:       .ash_history
d/d 3916:       .ssh
```
If we take a look in the `ssh` folder:
```
$ fls -o 206848 disk.img 3916
r/r 2345:       id_ed25519
r/r 2346:       id_ed25519.pub
```
The one ending with `.pub` is the public key. We will probably log in using the private key. Let's take a look at the contents:
```
$ icat -o 206848 disk.img 2345
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
```
Looks legit! Let's save the contents to a key file using `icat -o 206848 disk.img 2345 > key_file`. We should now be able to log in:
```
$ ssh -i key_file -p 58852 ctf-player@saturn.picoctf.net
The authenticity of host '[saturn.picoctf.net]:58852 ([18.217.86.78]:58852)' can't be established.
ECDSA key fingerprint is SHA256:0L/+wJ14/Sk4s6Ue+TxXnAW7qNBuaMeIxA9dXp2zzaU.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[saturn.picoctf.net]:58852,[18.217.86.78]:58852' (ECDSA) to the list of known hosts.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for 'key_file' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "key_file": bad permissions
```
Looks like we need to make the user and group have no permissions (currently their [permission flags are 4 meaning they can read](https://www.computerhope.com/unix/uchmod.htm)). To do that we can use `sudo chmod 600 key_file` and we can use `ls -l` to check the permissions of all the files in the directory. Let's try connecting again:
```
$ ssh -i key_file -p 63472 ctf-player@saturn.picoctf.net
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.13.0-1017-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@challenge:~$
```
We're in now! Let's see what's in the directories:
```
ctf-player@challenge:~$ ls -a
.  ..  .cache  .ssh  flag.txt
ctf-player@challenge:~$ cat flag.txt
picoCTF{k3y_5l3u7h_af277f77}ctf-player@challenge:~$ SConnection to saturn.picoctf.net closed by remote host.
Connection to saturn.picoctf.net closed.
```
We see a `flag.txt` and check out its contents. Nice.
## Flag
picoCTF{k3y_5l3u7h_af277f77}
