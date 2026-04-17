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
    password =  input("Enter Your Password: ")
    #check for valid length
    if len(password) < 8:
         raise ValueError('The password must be at least 8 characters long')

    #states 
    hasUpper = False
    hasLower = False
    hasDigit = False

    for ch in password:
        if ch.isupper():
            hasUpper= True
        elif ch.islower():
            hasLower = True
        elif ch.isdigit():
            hasDigit = True
    if hasUpper and hasLower and hasDigit:
        print('Valid, done.')
    else:
       raise ValueError('Need A-Z, a-z & 0-9')
except ValueError as error:
    print(f"INVALID PASSWORD. Error: {error}")
    
