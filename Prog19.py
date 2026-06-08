# Loan Eligibility Checker – Check eligibility using age, income, and credit score

age = int(input("Enter your age: "))
income = float(input("Enter your annual income: "))
credit_score = int(input("Enter your credit score: "))
if age >= 18 and income >= 30000 and credit_score >= 700:
    print("You are eligible for the loan.")
else:
    print("You are not eligible for the loan.")
    