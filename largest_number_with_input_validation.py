while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        break
    except ValueError:
        print("Invalid input. Please enter number only.")

if num1 > num2 and num1 > num3:
    print("The largest number is num1:", num1)
elif num2 > num1 and num2 > num3:
    print("The largest number is num2:", num2)
elif num3 > num1 and num3 > num2:
    print("The largest number is num3:", num3)
elif num1 == num2 and num1 > num3:
    print("num1 and num2 are equal but larger than num3:", num1)
elif num1 == num3 and num1 > num2:
    print("num1 and num3 are equal but larger than num2:", num1)
elif num2 == num3 and num2 > num1:
    print("num2 and num3 are equal but larger than num1:", num2)
else:
    print("All numbers are equal")
    

