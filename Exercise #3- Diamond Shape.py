# Exercise 3:  Diamond Shape (advance topic):

# Write a Python function named print_diamond that takes an odd integer n as an argument and prints a diamond shape with a width of n using the * character.
# For n = 5, the output should be:
#     *
#   ***
# *****
#   ***
#     *
# Note: If an even number is passed, the function should return "Please provide an odd integer."

def print_diamond():
    while True:
        try:
            n = int(input("\nEnter an odd integer as width of a diamond: "))
            if n % 2 != 0:
                for i in range(n // 2 + 1):
                    print(" " * (n // 2 - i) + "*" * (2 * i + 1))
                for i in range(n // 2 - 1, -1, -1):
                    print(" " * (n // 2 - i) + "*" * (2 * i + 1))
                break
            else:
                print("Please provide an odd integer.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
        
print_diamond()