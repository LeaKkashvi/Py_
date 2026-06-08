#Triangle type checker-Equilateral, Isosceles or Scalene

a = float(input("Enter the length of 1st side: "))
b = float(input("Enter the length of 2nd side: "))
c = float(input("Enter the length of 3rd side: "))
if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or a == c:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
