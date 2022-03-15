# patchme.py
## Author
LT 'syreal' Jones
## Description
Can you get the flag? Run this [Python program](./patchme.flag.py) in the same directory as this [encrypted flag](./flag.txt.enc).
## Hints
(None)
## Approach
If we look at the code, we'll see it's supposed to run `level_1_pw_check` and if we look at the function, we see this:
```python
def level_1_pw_check():
    user_pw = input("Please enter correct password for flag: ")
    if( user_pw == "ak98" + \
                    "-=90" + \
                    "adfjhgj321" + \
                    "sleuth9000"):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), "utilitarian")
        print(decryption)
        return
    print("That password is incorrect")
```
It checks to see if the user inputted "ak98" + "-=90" + "adfjhgj321" + "sleuth9000" which means the password is "ak98-=90adfjhgj321sleuth9000".
```
$ python3 patchme.flag.py
Please enter correct password for flag: ak98-=90adfjhgj321sleuth9000
Welcome back... your flag, user:
picoCTF{p47ch1ng_l1f3_h4ck_4d5af99c}
```
Note to run Python, you will use either `python` or `python3`, not necessarily `python3`
## Flag
picoCTF{p47ch1ng_l1f3_h4ck_4d5af99c}