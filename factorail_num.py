def factorail(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print("The factorial of 5 is:", factorail(5))