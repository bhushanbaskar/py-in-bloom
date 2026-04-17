'''
problem statement:
String
Write a python program that accepts a string to setup a password with
following requirements:
 The password must be at least eight characters long
 It must contain at least one uppercase letter
 It must contain at least one lowercase letter
 It must contain at least one numeric digit
The program checks the validity of password.
'''

try:
    password = input("Enter Your Password: ")

    errors = []

    if len(password) < 8:
        errors.append("At least 8 characters required")

    if not any(ch.isupper() for ch in password):
        errors.append("Missing uppercase letter")

    if not any(ch.islower() for ch in password):
        errors.append("Missing lowercase letter")

    if not any(ch.isdigit() for ch in password):
        errors.append("Missing digit")

    if errors:
        raise ValueError(", ".join(errors))

    print("Valid, done.")

except ValueError as error:
    print(f"INVALID PASSWORD: {error}")
    
