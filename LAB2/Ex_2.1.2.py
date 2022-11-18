#02.1.2 Resistances. Consider the following circuit. 

#Write a program that, starting from the resistance of the three resistors, given by the user, calculates the total resistance, using Ohm's law

def resistance(R1, R2, R3):
    R1_float = float(R1)

    R2_float = float(R2)

    R3_float = float(R3)

    # Since R2 and R3 are parallel therefore:
    R2_3_total = (R2_float * R3_float) / (R2_float + R3_float)

    # R1 and R_2_3_total are in series therefore:
    R_total = R1_float + R2_3_total

    #print the final results up to 2 decimal places
    print(f"The total Resistance of the Circuit is {R_total:0.2f} Ω")


if __name__ == "__main__":
    R1 = input(f"Please enter your first resistance R1: ")

    R2 = input(f"Please enter your second resistance R2: ")

    R3 = input(f"Please enter your third resistance R3: ")

    resistance(R1, R2, R3)

