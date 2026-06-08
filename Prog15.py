# Yearly Bonus Calculator – Calculate employee bonus using experience

years = int(input("Enter years of experience: "))
if years < 2:
    bonus = 0
elif years < 5:
    bonus = 2000
elif years < 10:
    bonus = 10000
else:
    bonus = 150000
print("The yearly bonus is:", bonus)
