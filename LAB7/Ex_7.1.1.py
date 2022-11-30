"""
07.1.1 Sum with alternating signs. Write a program that receives as input a sequence of integers 
(terminated by an empty line), and that calculates the alternating sum of its elements. For example, if 
the program reads the data 1 4 9 16 9 7 4 9 11, it must calculate and display 
1 - 4 + 9 - 16 + 9 - 7 + 4 - 9 + 11 = –2. 

"""
def alternate_sum(length):
    total = 0
    arr_num = [0]*length
    for i in range(length):
        arr_num[i] = int(input(f"{i+1}. Enter your number: "))

    for i in range(length):

        if (i%2==0):
            total += arr_num[i]
        else:
            total -= arr_num[i]

    print(f"The final result of alternate sum calculator is: {total}")

if __name__ == '__main__':
    number = int(input("Please enter the length of your array: "))
    alternate_sum(number)


