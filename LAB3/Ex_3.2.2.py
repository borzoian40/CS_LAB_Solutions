"""
Problem 3.2.2 - Write a program that translates a letter grade entered by the user into the 
corresponding numerical grade and prints it. The letter grades are 'A', 'B', 'C', 'D' and 'F', 
possibly followed by a + or – sign. Their numerical values are, in order, 4.0, 3.0, 2.0, 1.0 and
0.0. 'F+' and 'F–' grades do not exist. A + sign increases the numerical grade by 0.3, while a –
sign decreases it by the same amount. The 'A+' grade is equal to 4.0. [P3.12]
"""
##### First Approach #####

def main(grade):
    score = 0
    if grade == "A+":
        score = 4.3
    elif grade == "A":
        score = 4.0
    elif grade == "A-":
        score = 3.7
    elif grade == "B+":
        score = 3.3
    elif grade == "B":
        score = 3.0
    elif grade == "B-":
        score = 2.7
    elif grade == "C+":
        score = 2.3
    elif grade == "C":
        score = 2.0
    elif grade == "C-":
        score = 1.7
    elif grade == "D+":
        score = 1.3
    elif grade == "D":
        score = 1.0
    elif grade == "D-":
        score = 0.7
    else:
        print("Unfortunately, you have to redo the test.")
    return score


if __name__ == "__main__":
    result = (input("Please enter your grade: "))
    print(f"The numeric value is: {main(result)}")

##### Second Approach #####

grade = input("Please enter your grade: ")
grade = grade.upper()

if grade[0] == "A":
    score = 4.0
elif grade[0] == "B":
    score = 3.0
elif grade[0] == "C":
    score = 2.0
elif grade[0] == "D":
    score = 1.0
else:
    score = 0.0

# Handle the + or - if it is present.
if len(grade) > 1 and grade[0] != "F":
    if grade[1] == "+":
        score += 0.3
    elif grade[1] == "-":
        score -= 0.3
else:
    print("Unfortunately, you have to redo the test.")

#Final score
print(f"The numeric value of your grade is: {score}")
    
   
