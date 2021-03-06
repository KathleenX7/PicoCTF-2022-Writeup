# bloat.py

## Author

LT 'SYREAL' JONES

## Description

Can you get the flag?
Run this [Python program](./bloat.flag.py) in the same directory as this [encrypted flag](./flag.txt.enc).

## Hints

(None)

## Approach

I first looked at the encrypted flag by changing it to a .txt file. This showed the following:
```
 5*
\^F U[]Y1V, U[
P
W
```

I decided to look at the code instead and determine what it did. All strings are written from the characters in the String `a` (e.g. `a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]`) so I just printed the them to know what they said.

* `arg444` is the flag
* `arg432` is "Please enter correct password for flag:"
* `arg133(arg432)` asks for a password which is "happychance"
* `arg112()` prints "Welcome back... your flag, user:"

The part that encodes the flag is `arg423 = arg111(arg444)`. 

```python
def arg111(arg444):
  return arg122(arg444.decode(), a[81]+a[64]+a[79]+a[82]+a[66]+a[64]+a[75]+\
a[75]+a[72]+a[78]+a[77])
```

Looking at the code for the function arg111, it calls the function arg122 with the flag and the word "rapscallion"

```python
def arg122(arg432, arg423):
    arg433 = arg423
    i = 0
    while len(arg433) < len(arg432):
        arg433 = arg433 + arg423[i]
        i = (i + 1) % len(arg423)        
    return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(arg432,arg433)])
```

The encoded text is the xor or the characters in the flag and "rapscallion".

Looking back at the encrypted file, I put it into a hex editor which gave these integer values:
```
2 8 19 28 32 53 42 23 13 92 94 16 7 5 70 0 85 91 93 89 1 49 20 86 7 44 0 85 91 10 80 10 87 17 28
```

I made a program to find the flag. :

```java
public class pthon {
    public static void main(String[]args){
        int[] a = {2,8,19,28,32,53,42,23,13,92,94,16,7,5,70,0,85,91,93,89,1,49,20,86,7,44,0,85,91,10,80,10,87,17,28};
        String s = "rapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallionrapscallion"; //pasted rapscallion many times so that the length is greater than the flag
        for(int i=0; i < a.length; i++){
            System.out.print((char)(a[i] ^ s.charAt(i))); //inverse of xor is xor
        }
    }
}
```

## Flag

picoCTF{d30bfu5c4710n_f7w_c47f9e9c}
