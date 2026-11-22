a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Answer =", a + b)
elif choice == 2:
    print("Answer =", a - b)
elif choice == 3:
    print("Answer =", a * b)
elif choice == 4:
    if b != 0:
        print("Answer =", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid choice")
