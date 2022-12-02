def find_Local_Maxima(length, array):
    # An array to store the indices of the local maxima values.
    maxima = []
    
    #Check if the value located in the first index is greater than the adjacent.
    if (array[0] > array[1]):
        maxima.append(0)
    
    #Iterate through the array to check for the local maxima

    for i in range(1, length - 1):
        if (array[i - 1] < array[i] > array[i + 1]):
            maxima.append(i)
    #If the last element is greater than the previous element.
    if (array[-1] > array[-2]):
        maxima.append(0)
        
    #Check whether the array is null or not.    
    if (len(maxima) > 0):
        print("Indices where the local maxima is located: ")
        print(*maxima)
    else:
        print("There are no local maxima.")


if __name__ == "__main__":
    length = int(input("Please enter the length of your array: "))
    array = [0] * length

    for i in range(length):
        array[i] = int(input(f"{i + 1}. Enter your number: "))

    find_Local_Maxima(length, array)
