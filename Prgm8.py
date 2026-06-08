#Discount calculator- discunt based on purchase amount

amt=float(input("Enter the purchase amount: "))
if amt >= 1000:
    discount = amt * 0.1
    print("You get a 10% discount of:", discount)
    amt-= discount
    print("Purchase amount after discount:", amt)
elif amt >= 500:
    discount = amt * 0.05
    print("You get a 5% discount of:", discount)
    amt-= discount
    print("Purchase amount after discount:", amt)
else:
    discount = 0
    print("No discount applicable.")

 