"""
07.1.6 Ordered list. Write a program that generates a sequence of 20 random integer values between 
0 and 99, then displays the generated sequence, orders it, and displays it again, sorted.
Use the sort() method.

"""

import random

def ordered():
    arr = [0] * 20
    sortedarr = arr
    for i in range(20):
        arr[i] = random.randint(0, 99)

    print(arr)
    print("********")
    arr.sort()
    print(sortedarr)


if __name__ == "__main__":
    ordered()
