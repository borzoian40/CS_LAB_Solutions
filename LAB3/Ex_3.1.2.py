"""

03.1.2 Identikit of the string. Write a program that reads a string and displays the appropriate 
messages, after checking if: 
I. it contains only letters;
II. it contains only capital letters;
III. it contains only lowercase letters;
IV. it contains only digits;
V. it contains only letters and digits;
VI. it starts with a lowercase letter;
VII. it ends with a point.

"""
def main(input_message):

    if input_message.isalpha():
        print("The given input contains only letters.")
    elif input_message.isdigit():
        print("The given input contains only digits.")

    if input_message.isalpha and input_message.isupper():
        print("The given input contains only uppercase letters.")
    elif input_message.isalpha and input_message.islower():
        print("The given input contains only lowercase letters.")

    if input_message.alnum():
        print("The given input contains letters and digits only.")

    if input_message[0].islower():
        print("The given input starts with a lowercase letter.")

    if input_message.endswith("."):
        print("The given input is a sentence!")
