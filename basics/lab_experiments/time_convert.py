'''
problem statement:
Write a python program that accepts seconds as input of type integer. The
program should convert seconds in hours, minutes and seconds. Output
should like this :
Enter seconds: 12200
Hours: 3
Minutes: 23
Seconds: 20
'''
try:
    
    inputseconds = int(input("Enter No. of Seconds: "))

    if inputseconds < 0:
        raise ValueError("Seconds cannot be negative.")
    hours = inputseconds // 3600
    minutes = (inputseconds % 3600) // 60
    seconds = (inputseconds % 3600) % 60

    #result
    print(f'''
    Hours: {hours}
    Minutes: {minutes}
    Seconds: {seconds}
    ''')
except ValueError as e:
    print(f"Invalid input: {e}")