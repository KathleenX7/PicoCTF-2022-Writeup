# unpackme.py

## Author

LT 'SYREAL' JONES

## Description

Can you get the flag?
Reverse engineer this [Python program](./unpackme.flag.py).

## Hints

(None)

## Approach

I wasn't able to run the program on my computer so I tried running it on repl.it. It then asked for a password so I tried changing `exec(plain.decode())` to `print(plain.decode())`. It outputted:

```python
pw = input('What\'s the password? ')

if pw == 'batteryhorse':
  print('picoCTF{175_chr157m45_8aef58d2}')
else:
  print('That password is incorrect.')
```

## Flag

picoCTF{175_chr157m45_8aef58d2}
