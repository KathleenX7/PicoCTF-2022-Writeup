# credstuff

## Author

WILL HONG / LT 'SYREAL' JONES

## Description

We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it?
Download the [leak](./leak.tar) here.
The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.

## Hints

1. Maybe other passwords will have hints about the leak?

## Approach

I created a program to find the password of `cultrits` (another option is just to search "{" in the password file):

```java
import java.io.File; 
import java.io.FileNotFoundException; 
import java.util.Scanner;

public class credstuff {
    public static void main(String[] args) {
        try {
            File user = new File("usernames.txt");
            File pass = new File("passwords.txt");
            Scanner userIn = new Scanner(user);
            Scanner passIn = new Scanner(pass);
            while (userIn.hasNextLine()) {
                String password = passIn.nextLine();
                String username = userIn.nextLine();
                if(username.equals("cultiris")){
                    System.out.println(password);
                    return;
                }
            }
            userIn.close();
            passIn.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
```

This gave the password: cvpbPGS{P7e1S_54I35_71Z3}
If you search up "pico" on the password file, it gives "pICo7rYpiCoU51N6PicOr0t13".
I put the password in a rot13 website and found the flag.

## Flag

picoCTF{C7r1F_54V35_71M3}
