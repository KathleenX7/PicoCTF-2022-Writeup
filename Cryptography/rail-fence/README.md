# rail-fence
## Author
Will Hong
## Description
A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails.  
Can you decrypt it?  
Download the message [here](./message.txt).  
Put the decoded message in the picoCTF flag format, `picoCTF{decoded_message}`.
## Hints
1. Once you've understood how the cipher works, it's best to draw it out yourself on paper
## Approach
We can use [bocentriq](https://www.boxentriq.com/code-breaking/rail-fence-cipher) to decode the flag. The site says to use 4 rails. The result is: "The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_55228140"
## Flag
picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_55228140}