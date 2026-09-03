def main():
    # Prompt the user for two numbers
    # We use float() to allow for both whole numbers and decimals
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum
    total = num1 + num2

    # Display the result
    print(f"The sum of {num1} and {num2} is: {total}")

if __name__ == "__main__":
    main()