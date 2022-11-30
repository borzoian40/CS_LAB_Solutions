"""
06.1.4 Bank Balance. Write a function that calculates the balance of a bank account by crediting interest annually. 
The function receives as parameters: the number of years, the initial balance, and the annual interest rate. 
"""
def final_value(savings, interest_Rate, year):
    value = float(savings * ((1 + interest_Rate / 100) ** year))
    print(f"The final value after {year} year/s is: {value:0.2f}$")


if __name__ == "__main__":
    savings = int(input("Please enter your savings: "))
    interest = int(input("Please enter the interest rate of your bank: "))
    count_year = int(input("For how many years do you want your money to be in this bank?: "))

    final_value(savings, interest, count_year)
