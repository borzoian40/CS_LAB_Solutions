"""
03.1.5 Matter of logic. Write a program that takes as input an integer number x and displays the 
following expressions on the screen, along with their truth values. Test the program with numerous 
values of x.
I. x > 0 and x < 100
II. x > 0 or x < 100
III. x > 0 or 100 < x
IV. x > 0 and x < 100 or x == -1

"""
def main(number):
    integer_number = int(number)
    i_value = True

    #Condition 1
    if (integer_number > 0 and integer_number < 100):
        print(f"x > 0 and x < 100: {i_value}")
    else:
        print(f"x > 0 and x < 100: {not i_value}")

    #Condition 2
    if (integer_number > 0 or integer_number < 100):
        print(f"x > 0 or x < 100: {i_value}")
    else:
        print(f"x > 0 or x < 100:  {not i_value}")


    #Condition 3
    if (integer_number > 0 or 100 < integer_number):
        print(f"x > 0 or 100 < x: {i_value}")
    else:
        print(f"x > 0 or 100 < x: {not i_value}")

    #Condition 4
    if (integer_number > 0 and integer_number < 100 or integer_number == -1):
        print(f"x > 0 and x < 100 or x == -1: {i_value}")
    else:
        print(f"x > 0 and x < 100 or x == -1: {not i_value}")




if __name__ == "__main__":
    number = int(input("Please type your number: "))
    main(number)
