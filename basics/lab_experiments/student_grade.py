'''
problem statement: 
Conditional Structures
The marks obtained by a student in 3 different subjects are input by the
user. Python program should calculate the average marks obtained in 3
subjects and display the grade. The student gets a grade as per the
following rules:
Average Grade
90-100 O
80-89 A
70-79 B
60-69 C
40-59 D
0-39 F
'''
#the problem statement is not well defined what about if avg is 89.5
#let's redefine : just assume gtearter or equal than lower limit

try:
    
    physics = float(input("Enter Marks of Physics :"))
    chemistry = float(input("Enter Marks of Chemistry :"))
    math = float(input("Enter Marks of Math :"))
    #if invalid marks are entered
    if not ( 0<= physics <= 100 and 0<= chemistry <= 100 and 0<= math <= 100 ):
        raise ValueError("marks should be in range 0 to 100")
    
    #if marks are valid calc average
    average = (physics + chemistry + math)/3

    #Grades
    if average >=90:
        grade = "O"
    elif average >=80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >=40:
        grade = "D"
    else:
        grade = "F"

    print(f'''
    Average : {average:.2f}
    Grade: {grade}
 ''')
except ValueError as e:
    print(f'error: {e}')