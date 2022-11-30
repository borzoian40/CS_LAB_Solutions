"""
07.1.2 List of random numbers. Write a program that initializes a list with ten random integers between 1 and 100 and then displays, on four successive lines: 
I. All elements of even index; 
II. All the elements that are even; 
III. All elements in reverse order; 
IV. The first and the last element.

"""
from random import randint


def random_number():
    listarray = [] * 10
    for i in range(1, 11):
        listarray.append(randint(1, 101))

    even_index = [] * 10
    even_element = [] * 10
    reverse_listarray = [] * 10
    for j in range(0, 10):
        if j % 2 == 0:
            even_index.append(listarray[j])
        if listarray[j] % 2 == 0:
            even_element.append(listarray[j])

    # 1. Every element at an even index
    print(even_index)
    # 2. Every even element
    print(even_element)
    # 3. All elements in reverse order
    print(listarray[::-1])
    # 4. Only the first and last element
    print(listarray[0], listarray[len(listarray) - 1])

    print(f"The original random array: {listarray}")


random_number()

