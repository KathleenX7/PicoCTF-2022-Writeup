# unpackme
## Author
LT 'syreal' Jones
## Description
Can you get the flag?  
Reverse engineer this [binary](./unpackme-upx).
## Hints
1. What is UPX?
## Approach
Let's start off by addressing the hint. If we search up [UPX](https://en.wikipedia.org/wiki/UPX) and read some things about it, we'll learn it compresses things. After digging through the Wikipedia page a bit more, we can find the source code and [download it](https://github.com/upx/upx/releases/tag/v3.96). Now let's unpack it:
```
upx -d unpackme-upx
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2020
UPX 3.96w       Markus Oberhumer, Laszlo Molnar & John Reiser   Jan 23rd 2020

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
   1002408 <-    379116   37.82%   linux/amd64   unpackme-upx

Unpacked 1 file.
```
After unpacking, we can open the file in [Ghidra](https://ghidra-sre.org/) and check out the main function:
```c

undefined8 main(void)

{
  long in_FS_OFFSET;
  int local_44;
  char *local_40;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined4 local_20;
  undefined2 local_1c;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_38 = 0x4c75257240343a41;
  local_30 = 0x30623e306b6d4146;
  local_28 = 0x3366353630486637;
  local_20 = 0x5f64675f;
  local_1c = 0x4e;
  printf("What\'s my favorite number? ");
  __isoc99_scanf(&DAT_004b3020,&local_44);
  if (local_44 == 0xb83cb) {
    local_40 = (char *)rotate_encrypt(0,&local_38);
    fputs(local_40,(FILE *)stdout);
    putchar(10);
    free(local_40);
  }
  else {
    puts("Sorry, that\'s not it!");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```
The important line here is `if (local_44 == 0xb83cb)` and if we put 0xb83cb in an [online convertor](https://www.rapidtables.com/convert/number/hex-to-decimal.html), we get 754635.
```
$ ./unpackme-upx
What's my favorite number? 754635
picoCTF{up><_m3_f7w_ed7b0850}
```
## Flag
picoCTF{up><_m3_f7w_ed7b0850}