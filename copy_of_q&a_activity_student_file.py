# -*- coding: utf-8 -*-
"""Copy of Q&A activity student file.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/vidyapramod/cfb61aa8a3f942da19733a3cfaca63bd/copy-of-q-a-activity-student-file.ipynb

## 1. Complete the following code to find the area of an equilateral triangle. Output should be as displayed
"""

import math
side = float(input("Enter the side of the equilateral triangle: "))
area = math.sqrt(3)/4*pow(side,2)

"""## 2. Write a program to count the number of each characters in a string"""

string=str(input('Enter a string'))
str=[]
for i in string:
    if i in str:
        continue
    else:
        str.append(i)
        print(i,"=",string.count(i))

"""## Write a program to find the area and perimeter of a rectangle using functions"""

length=int(input('enter length '))
breadth=int(input('enter breadth '))
def area(length,breadth):
    print('area=',length*breadth)
area(length,breadth)
def perimeter(length,breadth):
    print('perimeter=',2*(length+breadth))
perimeter(length,breadth)

"""## 4. Write a program to print the fibonacci series till a specified number"""

n=int(input('Enter a limit '))
i=0
v=1
c=0
while(c<n):
    print(i)
    s=i+v
    i=v
    v=s
    c=c+1

"""## 5. Complete the following code to find the minimum of 3 number using cinditional statements. Output should be as displayed"""

a,b,c = input("Enter three numbers followed by  : ").split()

print("First number :",a)
print("Second number :",b)
print("Third number :",c)
if(a==b==c):
    print("Entered numbers are equal!!!")
elif(a<b):
    if(a<c):
         print(a," is smallest")
    else:
        print(c," is smallest")
elif(b<c):
    print(b," is smallest")
else:
     print(c," is smallest")



"""## 6. Write a program to print star pyramind. The number of rows should be taken as input from the user"""

r=int(input('enter no of rows'))
for i in range(r):
    for j in range(i+1):
        print('*', end='')
    print('\n')

"""## 7. Complete the following code to convert hour into seconds. Output should be as displayed"""

def to_seconds(t):
    return t
time_in_hours=int(input('Enter time in Hours'))

print(time_in_hours ," Hour is equal to" ,to_seconds(time_in_hours*60*60)," Seconds")

"""## 8. Write a program to print multiplication table as below"""

a=int(input('Enter a number to find the multiplication table '))
i=1
while(i<=10):
    print(i,'*',a,'=',i*a,'\n')
    i=i+1

"""## 9. Write a program to take your 5 favorite food as list and print each as 'I like Biriyani'"""

foods=list(input('Enter favourite foods list followed by space').split())
for f in foods:
    print('I like',f)

"""## 10. Find error(s) in the following code(if any) and rewrite code.


"""

x=int(input('Enter the value of x:'))
for y in range(0,10):
     if x==y:
          print("They are equal")
     else:
         print("they are unequal")