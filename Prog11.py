# ATM Withdrawal system - Validate balance, withdraw amount and minimum balance

n = float(input("Enter your current balance: "))
w = float(input("Enter the amount to withdraw: "))
if w>n:
    print("Insufficient balance.")
elif n-w < 1000:
    print("Cannot withdraw. Minimum balance of 1000 must be maintained.")
else:
    n -= w
    print("Withdrawal successful!! Remaining balance:", n)
    


