# Menu-driven program to check prime numbers,palindrome,factorial, find fibonacci , generate fibonacci, armstrong number

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
    
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = [0, 1]
        for i in range(2, n):
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

def is_armstrong(n):
    num_str = str(n)
    l = len(num_str)
    s = sum(int(digit) ** l for digit in num_str)
    return s == n

def main():
    while True:
        print("\nMenu:")
        print("1. Check Prime Number")
        print("2. Check Palindrome")
        print("3. Calculate Factorial")
        print("4. Find Fibonacci Number")
        print("5. Generate Fibonacci Sequence")
        print("6. Check Armstrong Number")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            num = int(input("Enter a number to check if it is prime: "))
            if is_prime(num):
                print(num, "is a prime number.")
            else:
                print(num, "is not a prime number.")
        
        elif choice == '2':
            num = int(input("Enter a number to check if it is a palindrome: "))
            if is_palindrome(num):
                print(num, "is a palindrome.")
            else:
                print(num, "is not a palindrome.")
        
        elif choice == '3':
            num = int(input("Enter a number to calculate its factorial: "))
            result = factorial(num)
            if result is not None:
                print("Factorial of", num, "is", result)
            else:
                print("Factorial is not defined for negative numbers.")
        
        elif choice == '4':
            n = int(input("Enter the position of the Fibonacci number to find: "))
            result = fibonacci(n)
            if result is not None:
                print(f"The {n}th Fibonacci number is {result}.")
            else:
                print("Invalid input for Fibonacci sequence.")
        
        elif choice == '5':
            n = int(input("Enter the number of Fibonacci numbers to generate: "))
            result = generate_fibonacci(n)
            if result:
                print(f"The first {n} Fibonacci numbers are: {result}")
            else:
                print("Invalid input for generating Fibonacci sequence.")
        
        elif choice == '6':
            num = int(input("Enter a number to check if it is an Armstrong number: "))
            if is_armstrong(num):
                print(num, "is an Armstrong number.")
            else:
                print(num, "is not an Armstrong number.")
        
        elif choice == '7':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":    
    main()