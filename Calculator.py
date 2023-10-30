# Define the calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Main calculator loop
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'clear' to start over")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "clear":
        continue

    operation = None
    result = None
    numbers = []

    while True:
        try:
            num = float(input("Enter a number (or 'done' to perform the current operation): "))

            if operation is None:
                numbers.append(num)
            else:
                result = operation(result, num)

            print("Current result:", result)
        except ValueError:
            if user_input == "add":
                operation = add
            elif user_input == "subtract":
                operation = subtract
            elif user_input == "multiply":
                operation = multiply
            elif user_input == "divide":
                operation = divide

            if not operation:
                print("Unknown input. Please enter a valid operation.")
                break

            if len(numbers) >= 2:
                result = operation(numbers[0], numbers[1])

            print("Current result:", result)

        if user_input != "add" and user_input != "subtract" and user_input != "multiply" and user_input != "divide":
            print("Unknown input. Please enter a valid operation.")
            break
