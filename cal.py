import sys

def calculate(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        return "Error: Unknown operation. Please use add, subtract, multiply, or divide."

def main():
    # Check if the user provided the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <operation> <num1> <num2>")
        print("Example: python calculator.py add 10 5")
        sys.exit(1) # Exit with an error code so Jenkins knows it failed

    # Grab the inputs from the command line
    operation = sys.argv[1].lower()
    
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: Please provide valid numbers for num1 and num2.")
        sys.exit(1)

    # Perform the calculation and print the result
    result = calculate(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()