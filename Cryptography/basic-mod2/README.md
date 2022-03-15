# basic-mod2

## Author

WILL HONG

## Description

A new modular challenge!
Download the message [here](./message.txt).
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

## Hints

1. Do you know what the modular inverse is?
2. The inverse modulo z of x is the number, y that when multiplied by x is 1 modulo z
3. It's recommended to use a tool to find the modular inverses

## Approach

I modified the code from basic-mod2 to solve the question for me: 

```java
public class mod2{
    public static int inverse(int n){
        for(int i=0; i < 41; i++){
            if((n*i)%41 == 1){return i;}
        }return 0;
    }
    public static void main(String[] args){
        int[] list = {350, 372, 192, 354, 139, 337, 67, 311, 392, 338, 241, 414, 180, 277, 379, 294, 128, 117, 250, 404, 336, 350, 386};
        char[] chr = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '0','1','2','3','4','5','6','7','8','9', '_'};
        for(int i=0; i < list.length; i++){
            System.out.print(chr[inverse(list[i]) -1]); //index starts at 1 for basic-mod2
        }
    }
}
```

The code outputted "1NV3R53LY_H4RD_F6747912"

## Flag

picoCTF{1NV3R53LY_H4RD_F6747912}
