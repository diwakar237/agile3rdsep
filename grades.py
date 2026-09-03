import sys

def main():
    # Check if exactly three marks were provided
    if len(sys.argv) != 4:
        print("Usage: python marks.py <mark1> <mark2> <mark3>")
        print("Example: python marks.py 85 90 78")
        sys.exit(1)

    try:
        # Convert arguments to floats to support decimals
        mark1 = float(sys.argv[1])
        mark2 = float(sys.argv[2])
        mark3 = float(sys.argv[3])
    except ValueError:
        print("Error: Please provide valid numbers for the marks.")
        sys.exit(1)

    # Calculate Total and Average
    total = mark1 + mark2 + mark3
    average = total / 3

    # Define Pass Criterion: Average >= 40 AND all individual subjects >= 35
    if average >= 40 and mark1 >= 35 and mark2 >= 35 and mark3 >= 35:
        status = "PASS"
    else:
        status = "FAIL"

    # Display Results
    print("--- Student Results ---")
    print(f"Subject 1: {mark1}")
    print(f"Subject 2: {mark2}")
    print(f"Subject 3: {mark3}")
    print(f"Total Marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Final Status: {status}")

if __name__ == "__main__":
    main()