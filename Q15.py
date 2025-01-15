# Prompt for a year and determine if it’s a leap year. 365.242199

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):      
    print("Leap year")
else:
    print("Not a leap year")
