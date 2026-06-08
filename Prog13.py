# Login Authentication – Validate username and password
u= input("Enter username: ")
p= input("Enter password: ")

if u == "admin" and p == "password":
    print("Login successful.")
else:
    print("Invalid username or password.")