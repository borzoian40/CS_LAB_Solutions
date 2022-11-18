# 02.1.3 Digits: Write a program that stores in a constant a positive five-digit integer (therefore between 10000 and 99999), 
#and displays the individual digits of which it is composed. For example, having the number 16384, the program must display, on separate lines: 1 6 3 8 4.


def digits(number):

#First we create a variable called len_of_number for getting the length of our "number" string.
    len_of_number = len(number)
 #Then we introducea a variable called array_number which represents each character of the string in an array with size = len_of_number.
    array_number = number[0:len_of_number]
  #Now by iterating through the array, we print each element of the array in a single line.
    for index in range(len_of_number):
      
      
#if the index is not equal to the size of the array then print that character and end with a space.
        if (index!=len_of_number):
            print(array_number[index], end = " ")
#else just print the number.
        else:
            print(array_number[index], end = "")

if __name__ == "__main__":
  
    input = input("Please enter your number: ")
    digits(input)
