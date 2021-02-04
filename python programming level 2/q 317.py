import math
a=int(input("Enter first side: "))
b=int(input("Enter second side: "))
c=int(input("Enter third side: "))
s=(a+b+c)/2
ar=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"Area of the triangle is:  {round(ar,2)}")
