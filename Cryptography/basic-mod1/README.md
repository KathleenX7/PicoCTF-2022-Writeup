# basic-mod1

## Author

WILL HONG

## Description

We found this weird message being passed around on the servers, we think we have a working decrpytion scheme.
Download the message [here](./message.txt).
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Hints

1. Do you know what mod 37 means?
2. mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

## Approach

I wrote some code to find the values for me:

```java
public class mod1{
    public static void main(String[] args){
        int[] list = {128, 63, 131, 198, 262, 110, 309, 73, 276, 285, 316, 161, 151, 73, 219, 150, 145, 217, 103, 226, 41, 255};
        char[] chr = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '0','1','2','3','4','5','6','7','8','9', '_'};
        for(int i=0; i < list.length; i++){
            System.out.print(chr[list[i]%37]);
        }
    }
}
```

The code outputted "R0UND_N_R0UND_8C863EE7"

## Flag

picoCTF{R0UND_N_R0UND_8C863EE7}
