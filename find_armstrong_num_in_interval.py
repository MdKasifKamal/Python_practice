lower = int(input("Enter the lower bound of the interval: "))
upper = int(input("Enter the upper bound of the interval: "))

for num in range(lower, upper + 1):
    sum = 0
    temp = num
    order = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** order
        temp = temp // 10
    if num == sum:
        print(num, "is an Armstrong number")    