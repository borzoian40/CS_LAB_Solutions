"""
04.1.6 Prime numbers. Write a program that asks the user for an integer number and shows all the 
prime numbers lower or equal to that number. Example: if the user inputs 20, the program shall 
output: 
2 
3 
5 
7 
11 
13 
17 
19 
"""

def is_prime_range(input):
    for num in range(2, input+1):

        for j in range(2, num):
            if (num % j == 0):
                break
        else:
            print(num)


if __name__ == "__main__":
    number = int(input("Please enter your number: "))
    is_prime_range(number)

