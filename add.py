import sys

def main():
    # Grab the numbers from the command line arguments
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    total = num1 + num2
    print(f"The sum of {num1} and {num2} is: {total}")

if __name__ == "__main__":
    main()