"""
05.1.3 Factoring of integers. Write a program that asks the user for an integer and then 
prints out all its factors. For example, when the user enters 150, the program should print
2
3
5
5
"""
def factors(number):

    while number != 1:
        for i in range(2, number + 1):
            if number % i == 0:
                print(i)
                number //= i


print(factors(125))
