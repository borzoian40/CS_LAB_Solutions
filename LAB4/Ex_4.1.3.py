"""
04.1.3 Shapes. Write a program that takes as an input an integer number n and prints a square and a 
rhombus filled with asterisks (*), with each side long n asterisks. Example: using n=4, the program 
shows: 
****
****
****
****
   *
  ***
 *****
*******
 *****
  ***
   *

"""
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(rows):
    for j in range(columns):
        print("*", end = "")
    print()

