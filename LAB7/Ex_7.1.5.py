"""
07.1.5. Write the same_set(a, b) function that checks if two lists contain the 
same elements, regardless of the order and ignoring the presence of duplicates. 
For example, the two lists 1 4 9 16 9 7 4 9 11 and 11 11 7 9 16 4 1 must be considered equal. 
The function must not modify the lists that have been passed as parameters. 

"""

def same_Set(arr1, arr2):
    if contained(arr1, arr2) and contained(arr2, arr1):
        print("They are the same list!")
    else:
        print("They are not the same.")


def contained(arr1, arr2):
    for element in arr1:
        if element not in arr2:
            return False
    return True


if __name__ == "__main__":
    length1 = int(input("Please enter the length of your first list: "))
    length2 = int(input("Please enter the length of your second list: "))

    list1 = [0] * length1
    list2 = [0] * length2
    print()
    print("***** First List *****")
    for i in range(length1):
        list1[i] = int(input(f"{i + 1}. Enter your number: "))
    print()
    print("***** Second List *****")
    for j in range(length2):
        list2[j] = int(input(f"{j + 1}. Enter your number: "))

    same_Set(list1, list2)
