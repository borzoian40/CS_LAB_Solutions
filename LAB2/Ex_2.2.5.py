"""
02.2.5 Registrations. The freshman of the students of a University is composed of two parts: a letter 
and a sequence of numbers. Write a program that, starting from two serial codes, shows them on 
the screen in ascending order based on the numerical part only. Tip: Use the default functions of
the Python language.
"""
    if int(student_id_1[1:])> int(student_id_2[1:]):
        print(student_id_2)
        print(student_id_1)
    else:
        print(student_id_1)
        print(student_id_2)

if __name__ == "__main__":

    print("Welcome!! Please enter two student id's.")
    student_id1 = input("Student 1: ")
    student_id2 = input("Student 2: ")
    main(student_id1, student_id2)
