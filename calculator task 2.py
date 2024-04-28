def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def calculator():
    while True:
        print("""
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Exit
        """)
        choice = int(input("Enter your choice: "))
        if choice == 5:
            break
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        else:
            print("Invalid choice. Please try again.")
            continue
        print(f"The result is {result}")

if __name__ == "__main__":
    calculator()
