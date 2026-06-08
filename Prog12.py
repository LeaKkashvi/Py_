#Find second largest among three numbers without sorting
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if a > b and a < c or a < b and a > c:
    print("Second largest number:", a)
elif b > a and b < c or b < a and b > c:
    print("Second largest number:", b)
else:
    print("Second largest number:", c)