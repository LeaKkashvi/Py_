#Movie Ticket Pricing – Calculate ticket price using multiple conditions

age = int(input("Enter your age: "))
r=input("Enter front row or back row (f/b): ")
if age < 3:
    price = 0
elif age < 12:
    price = 100
elif age < 60:
    price = 150
else:
    price = 120
if r == "f":
    price += 10
elif r == "b":
    price += 40
else:
    print("enter f or b,  Defaultning to back row.")
    price +=40

print("The ticket price is:", price)
