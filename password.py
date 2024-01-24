#! python3
# password.py - Detect strong password

import re


def password_detector():
    password = input("Enter your Password")
    return password


# Determine how strong a password is
def password_strong():
    passcode = password_detector()

    # Check for Uppercase and lowercase
    if not re.search(r'[a-z]', passcode) or not re.search(r'[A-Z]', passcode):
        return True

    # Check for digit
    if not re.search(r'\d', passcode):
        return True

    # Check for symbols
    if not re.search(r'[!@#$%^&*()_,./<>]', passcode):
        return True


result = password_strong()


if result:
    print("The password is not strong")
else:
    print("The password is strong")
