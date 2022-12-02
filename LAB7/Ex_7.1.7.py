"""
07.1.7 Add up without the minimum. Write the sum_without_smallest(v) function that 
calculates the sum of all the values of a list v, excluding the minimum value.
"""
def sum_without_smallest(arr):
    min = arr[0]
    index = 0
    for i in range(len(arr)):
        if arr[i] <= min:
            min = arr[i]
            index = i

    print(arr)

    arr.pop(index)
    print(arr)

    sum = 0
    for i in range(len(arr)):

        sum += arr[i]
      

    print(f"The sum is: {sum}")


if __name__ == "__main__":

    length = int(input("Please enter the length of your array: "))
    arr = [0] * length
    for i in range(length):
        arr[i] = int(input(f"{i + 1}. Enter your number: "))

    sum_without_smallest(arr)
