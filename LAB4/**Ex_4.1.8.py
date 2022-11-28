"""
04.1.8 Duplicate numbers. Write a program reading a sequence of integer numbers (the sequence 
ends with an empty line) and, after each acquisition, compute and shows only the adjacent duplicate 
numbers.
All adjacent duplicates. For example, if the input is 1 3 3 4 5 5 6 6 6 2, the 
program should print 3 5 6. 

"""
input_set = []
input_num = 0

while (input_num >= 0):

    input_num = int(input("Please enter a number or -1 to finish"))
    if (input_num < 0):
        break
    input_set.append(input_num)

print(input_set)

new_list = []
unique_list = []

for i in range(0,len(input_set)-1):
    if input_set[i]==input_set[i+1] or input_set[i] == input_set[i-1]:
        new_list.append(input_set[i])

[unique_list.append(item) for item in new_list if item not in unique_list]
print(unique_list)
