# substitution0
## Author
Will Hong
## Description
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?  
Download the message [here](./message.txt).
## Hints
1. Try a frequency attack. An online tool might help.
## Approach
A substitution cipher is a cipher that substitutes one thing for another. This might mean letters become symbols but in this case, it substitutes letters to other letters. A frequency analysis looks at how often a certain symbol appears since in languages, there are lettesr that appear more often than others. Luckily there are online tools available to solve monoalphabetical substitution ciphers for us so we don't need to do anything.  
If we paste the contents of [`message.txt`](./message.txt) into [decode.fr's monoalphabetical substituion solver](https://www.dcode.fr/monoalphabetic-substitution) and press "DECRYPT AUTOmATICALLY" it'll solve it for us.
## Flag
picoCTF{5UB5717U710N_3V0LU710N_AA1CC2B7}