num = int(input("Enter a number: "))

if num % 400 == 0 and num % 100 == 0:
    print("The year is a leap year")
elif num % 4 == 0 and num % 100 != 0:
    print("The year is a leap year")
else:
    print("The year is not a leap year")