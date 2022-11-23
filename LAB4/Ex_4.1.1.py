"""
4.1.1 
Integer numbers. Write a program reading a sequence of integer numbers (an empty string is the end of the sequence) 
and, after each input, executing and visualizing: 
I. Partial sums of every number acquired; the program must visualize the result of the 
calculations after each input.
As an example, if the input values are 1 7 2 9, the program shall visualize the partial sum 
of the numbers acquired after each input:
a. After the first input (1), the first acquired value: 1.
b. After the second input (7), the sum between the first and the second acquired 
values: 1 + 7 = 8.
c. After the third input (2), the sum between the first, the second, and the third 
acquired values: 1 + 7 + 2 = 10.
d. After the fourth input (9), the sum between the first, the second, the third, and the 
fourth values acquired: 1 + 7 + 2 + 9 = 19.
II. The minimum and the maximum values among the acquired ones.
III. How many acquired values are even, how many acquired values are odd. 
"""

number_str = int(input("How many numbers do you want in your list? "))
sum = 0
list_ofnumbers = [0] * number_str
list_even = []
list_odd_num = []

max = list_ofnumbers[0]

for index in range(number_str):
    number = int(input(f"{index + 1}. Type in your number: "))
    list_ofnumbers[index] = number
    if(number%2==0):
        list_even.append(number)
    else:
        list_odd_num.append(number)

    min = list_ofnumbers[0]
    sum += number
    if (list_ofnumbers[index] > max):
        max = list_ofnumbers[index]
    elif (list_ofnumbers[index] <= min):
        min = list_ofnumbers[index]


    print(
        f"The sum value is: {sum - number} + {number} = {sum}\nThe maximum value is: {max}.\nThe minimum value is: {min}")

print(f"The list of even numbers are: {list_even}\nThe list of odd numbers are: {list_odd_num}")
