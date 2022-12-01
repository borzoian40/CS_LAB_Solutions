"""
07.1.3 Remove the minimum value. Write a remove_min(v) function that removes the minimum 
value from a v list without using the min() function or the remove() method.
"""
def arrayfunction(length):
    integer = int(length)
    listarr = ([0] * integer)
    updatedlist = listarr
    for i in range(integer):
        listarr[i] = int(input(f"{i + 1}. Enter your number: "))
        updatedlist[i] = listarr[i]
    number = (listarr[0])
    index = 0
    
    #Finding the minimum number
    for i in range(integer):
        if listarr[i] <= number:
            number = listarr[i]
            index = i

    listarr.pop(index)
    print(f"The minimum number in our list is:  {number}")

    print(f"Updated array after removing minimum: {listarr}")


if __name__ == "__main__":
    number = int(input("Please enter the length of your array: "))
    arrayfunction(number)
