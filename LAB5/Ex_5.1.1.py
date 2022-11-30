"""
05.1.1 ATM. When you use an automated teller machine (ATM) with your bank card, you
need to use a personal identification number (PIN) to access your account. If a user fails
more than three times when entering the PIN, the machine will block the card. Assume that
the user’s PIN is “1234” and write a program that asks the user for the PIN no more than
three times, and does the following:
• If the user enters the right number, print a message saying, “Your PIN is 
correct”, and end the program.
• If the user enters a wrong number, print a message saying, “Your PIN is 
incorrect” and, if you have asked for the PIN less than three times, ask for it 
again.
• If the user enters a wrong number three times, print a message saying “Your 
bank card is blocked” and end the program.
"""
PIN = "1234"
count = 0


def main():
    pin = input("Please enter your PIN: ")
    check_pin(pin)


def check_pin(pin_number):
    global count

    while (count < 2):
        if (pin_number == PIN):
            print("Your PIN is correct! Welcome!")
            break

        elif (pin_number != PIN):
            print("Your PIN is incorrect! Please try again.")
            count += 1
            main()
            break
    print("Your bank account is blocked.")


main()
