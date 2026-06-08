#Simple Calculator

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = n1 + n2
elif operation == '-':
    result = n1 - n2
elif operation == '*':
    result = n1 * n2
elif operation == '/':
    if n2 != 0:
        result = n1 / n2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"
print("The result is:", result)
