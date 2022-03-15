# Safe Opener

## Author

MUBARAK MIKAIL

## Description

Can you open this safe?
I forgot the key to my safe but this program is supposed to help me with retrieving the lost key. Can you help me unlock my safe?
Put the password you recover into the picoCTF flag format like:
`picoCTF{password}`

## Hints

(None)

## Approach

Looking at the code, what sticks out is the encoded password `"cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz"` and a Base64 encoder. I put the encoded password in a base64 to text converter and got `pl3as3_l3t_m3_1nt0_th3_saf3`

## Flag

picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
