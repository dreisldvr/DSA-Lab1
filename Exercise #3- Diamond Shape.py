# Function to print a diamond shape
def print_diamond():
    while True:
        try:
            n = int(input("\nEnter an odd integer as width of a diamond: "))
            if n % 2 != 0:
                # Print the upper part of the diamond
                for i in range(n // 2 + 1):
                    print(" " * (n // 2 - i) + "*" * (2 * i + 1))
                # Print the lower part of the diamond
                for i in range(n // 2 - 1, -1, -1):
                    print(" " * (n // 2 - i) + "*" * (2 * i + 1))
                break
            else:
                print("Please provide an odd integer.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

# Call the function to print the diamond
print_diamond()
