def largest(a,b,c):
  if a>b and a>c:
    print("a is the largest number")
  elif b>a and b>c:
    print("b is the largest number")
  elif a==b and a==c:
    print("All numbers are equal")
  elif a==b and a>c:
    print("a and b are the equal but larger than c")
  elif a==c and a>b:
    print("a and c are the equal but larger than b")
  elif b==c and b>a:
    print("b and c are the equal but larger than a")
  else:
    print("c is the largest number")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
largest(a,b,c)