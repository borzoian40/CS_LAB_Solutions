"""
04.1.5 Prime numbers. Write a program that asks the user for an integer number and shows as an 
output a message showing whether the input number is prime.
"""
#First Approach#
def is_prime1(number):
  for i in range(2,number):
    if (number%i) == 0:
      return False
  return True

#Second Approach #You don’t have to loop all the way up to n – 1. You can instead run the loop only up to n/2.
def is_prime2(number):
  for i in range(2,int(number/2)):
    if (number%i) == 0:
      return False
  return True

#Third Approach 
#So instead of looping through all integers up to n/2, you may choose to run up to √n. And this is a lot more efficient than our previous approach.

import math
def is_prime3(number):
  for i in range(2,int(math.sqrt(number))+1):
    if (number%i) == 0:
      return False
  return True

