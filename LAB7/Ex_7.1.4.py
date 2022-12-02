"""
07.1.4 Local highs. Read a sequence of integers ended by a blank line. Print the position of the local 
maxima (numbers greater than both the previous and the next value) if there are any, otherwise print 
the message 'There are no local maxima'. 
Extension: if there are several pairs of local maxima, identify the two closest local maxima and print their position.
"""

def find_Local_Maxima(length, array):
    # An array to store the indices of the local maxima values.
    maxima = []

    if (array[0] > array[1]):
        maxima.append(0)


    for i in range(1, length - 1):
        if (array[i - 1] < array[i] > array[i + 1]):
            maxima.append(i)

    if (array[-1] > array[-2]):
        maxima.append(0)
    if (len(maxima)>0):
      print("Indices where the local maxima is located: ")
      print(*maxima)
    else:
      print("There are no local maxima.")
