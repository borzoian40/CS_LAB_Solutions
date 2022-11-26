
"""
 Words in reverse. Write a program that reads a word and outputs: 
I. The reversed word. If the user writes the string 'Hello', the program shall output
'olleH':
"""
def main(string):
    print(string[::-1])

if __name__ == "__main__":
    something = input("Please enter your name: ")
    main(something)
"""
II. The uppercase letters starting from the end. If the user writes the string 'HeLlO', the 
program shall output 'OLH'.
"""
def main(letters):
    upper_case = ""

    for i in range(len(letters)):
        if (letters[i] >= "A" and letters[i] <= "Z"):
            upper_case += letters[i]

    return (upper_case[::-1])


if __name__ == "__main__":
    something = input("Please enter your string: ")
    print(f"The reversed capital letters of your string are: {main(something)}")



