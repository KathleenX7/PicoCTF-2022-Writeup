# Bbbbloat
## Author
LT 'syreal' Jones
## Description
Can you get the flag?  
Reverse engineer this [binary](./bbbbloat).
## Approach
After opening the file in [Ghidra](https://ghidra-sre.org/), I looked through the functions. The function FUN_00101307 contained this:
```c

undefined8 FUN_00101307(void)

{
  char *__s;
  long in_FS_OFFSET;
  int local_48;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined8 local_20;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_38 = 0x4c75257240343a41;
  local_30 = 0x3062396630664634;
  local_28 = 0x35613066635f3d33;
  local_20 = 0x4e603234363266;
  printf("What\'s my favorite number? ");
  __isoc99_scanf();
  if (local_48 == 0x86187) {
    __s = (char *)FUN_00101249(0,&local_38);
    fputs(__s,stdout);
    putchar(10);
    free(__s);
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
The important part of this code it the line `if (local_48 == 0x86187)`, so if your input is the same as 0x86187 (hex) then you get the flag. Using [rapidtables](https://www.rapidtables.com/convert/number/hex-to-decimal.html) you can convert hex to decimal and get 549255.
```
$ ./bbbbloat
What's my favorite number? 549255
picoCTF{cu7_7h3_bl047_2d7aeca1}
```
## Flag
picoCTF{cu7_7h3_bl047_2d7aeca1}