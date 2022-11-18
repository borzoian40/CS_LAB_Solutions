#02.1.1 Two numbers. Write a program that stores two integers in two constants defined in code, and then displays them: 
#A. The sum; 
#B. The difference; 
#C. The product; 
#D. The average value; 
#E. The distance (i.e. the absolute value of the difference); 
#F. The maximum value (i.e. the greater of the two); 
#G. The minimum value (i.e. the lesser of the two).

#define a new function
def main(number1, number2):
    # a) Sum of the two numbers
    total_sum = number1 + number2
    print(f"{number1} + {number2} = {total_sum}")
    # b) Difference of the two numbers

    if (number1 > number2):
        difference = number1 - number2
        print(f"{number1} - {number2} = {difference}")
    else:
        difference = number2 - number1
        print(f"{number1} - {number2} = {difference}")

    # c) Multiplication of the two numbers

    product = number1 * number2
    print(f"{number1} x {number2} = {product}")

    # d) Average value of the two numbers

    average_value = (number1 + number2) / 2
    print(f"({number1} + {number2})/2 = {average_value}")

    # e)The absolute value of the difference
    absolute_distance = abs(number1 - number2)
    print(f"|{number1} - {number2}| = {absolute_distance}")

    # f)Maximum value
    max_number = max(number1, number2)
    print(f"Maximum value between {number1} and {number2} is {max_number}")

    # g) Minimum value
    min_number = min(number1, number2)
    print(f"Minimum value between {number1} and {number2} is {min_number}")


if __name__ == "__main__":
    
    input_num1 = int(input("Please enter your first number: "))
    input_num2 = int(input("Please enter your second number: "))

    main(input_num1, input_num2)
