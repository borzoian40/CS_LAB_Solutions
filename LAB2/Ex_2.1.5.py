"""
02.1.5 Electric force. According to Coulomb's law, the electric force (expressed in Newtons) between 
two charged charged particles, respectively, Q1 and Q2, separated by a distance r, is 
𝐹  =  (𝑄1 𝑄2)/(4 𝜋 𝜀 𝑟2)
 where 𝜀  =  8.854  ×  10−12 Farad / meter. Write a program that calculates and shows on screen 
the force relative to a pair of charged particles, allowing the user to choose the values Q1, Q2 (in 
Coulomb) and r (in meters). (2.43 pm)

"""

# ** is the symbol used for power
EPSILON = 8.854 * (10 ** (-12))
PI = 3.14


def main():
    Q1 = float(input("Q1 (in Coulomb): "))
    Q2 = float(input("Q2 (in Coulomb): "))
    distance = float(input("r (in meters): "))

    F = (Q1 * Q2) / (4 * PI * EPSILON * (distance ** 2))

    print(f"The electric force is {F:0.2f} N.")


if __name__ == "__main__":
    main()
