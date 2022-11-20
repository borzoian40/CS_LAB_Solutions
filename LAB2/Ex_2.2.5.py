"""
02.2.5 Registrations. The freshman of the students of a University is composed of two parts: a letter 
and a sequence of numbers. Write a program that, starting from two serial codes, shows them on 
the screen in ascending order based on the numerical part only. Tip: Use the default functions of
the Python language.
"""

def main():

    student_id_a = "S50123"
    student_id_b = "S41235"

    if int(student_id_a[1:])> int(student_id_b[1:]):
        print(student_id_a)
        print(student_id_b)
    else: 
        print(student_id_b)
        print(student_id_a)

if __name__ == "__main__":
    main()
