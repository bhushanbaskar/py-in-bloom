'''
problem statement:
Control structures
Floyd's triangle is a right-angled triangular array of natural numbers as
shown below:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
Write a python program to print the Floyd‟s triangle
'''

count = 1
row = int(input("How many rows you want: "))

for i in range(1,row+1):
    for j in range(1,i+1):
        print(count,end=' ')
        count +=1
    print()
    
