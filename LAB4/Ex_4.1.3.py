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
"""
Square pattern
"""
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(rows):
    for j in range(columns):
        print("*", end = "")
    print()
    
    
"""
Star pattern
"""

def main(row):
    column = int(row)
    i = 0
    while (i < column):
        j = column
        while (j > i+1):
            print(" ", end="")
            j -= 1
        k = 0
        while (k <= i):
            print("*", end="")
            k += 1
        l = 0
        while (l < i):
            print("*", end="")
            l += 1

        print()
        i += 1

    i1 = 0
    while (i1 < column - 1):
        j1 = 0
        while (j1 <= i1):
            print(" ", end="")
            j1 += 1

        k1 = column - 1
        while (k1 > i1):
            print("*", end="")
            k1 -= 1

        l1 = column - 2
        while (l1 > i1):
            print("*", end="")
            l1 -= 1
        print()
        i1 += 1


if __name__ == "__main__":
    row = int(input("Please enter the number of rows: "))
    main(row)
