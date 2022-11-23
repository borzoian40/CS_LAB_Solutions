"""
03.2.3 
The following algorithm yields the season (Spring, Summer, Fall, or Winter) for a given month and day.
If month is 1, 2, or 3, season = "Winter" 
Else if month is 4, 5, or 6, season = "Spring"
Else if month is 7, 8, or 9, season = "Summer"
Else if month is 10, 11, or 12, season = "Fall"
If month is divisible by 3 and day >= 21
If season is "Winter", season = "Spring" 
Else if season is "Spring", season = "Summer" 
Else if season is "Summer", season = "Fall" 
Else season = "Winter" 
Write a program that prompts the user for a month 
and day and then prints the season, as determined 
by this algorithm.
"""
def seasons(month, day):
    season = ""
    if (1<=month<=3):
        season = "Winter"
    elif (4<=month<=6):
        season = "Spring"
    elif (7<=month<=9):
        season = "Summer"
    elif (10<=month<=12):
        season = "Fall"

    if (month % 3 == 0) and day >= 21:
        if season == "Winter":
            season = "Spring"
        elif season == "Spring":
            season = "Summer"
        elif season == "Summer":
            season = "Fall"
        else:
            season = "Winter"

    return season


if __name__ == "__main__":
    month = int(input("Please type in your month: "))
    day = int(input("Please type in your day: "))

    print(f"The season is: {seasons(month, day)}")
