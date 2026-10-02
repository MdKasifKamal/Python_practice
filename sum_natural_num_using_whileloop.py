num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a positive number")
else:
 sum = 0
 while num > 0:
    sum = sum + num
    num = num -1
    
 print("The sum of natural numbers is:", sum)