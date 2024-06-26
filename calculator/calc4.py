# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print("Select operation.")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")

while True:
    # take input from the user
    choice = input("Enter choice (Add/Subtract/Multiply/Divide): ")

    # check if choice is one of the four options
    if choice in ('Add', 'Subtract', 'Multiply', 'Divide'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 'Add':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'Subtract':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'Multiply':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'Divide':
            print(num1, "/", num2, "=", divide(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")