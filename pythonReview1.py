# Function to get the temperature input from the user
def get_temperature():
    while True:
        try:
            # Ask the user to enter a temperature
            temp = float(input("\nEnter the temperature: "))
            return temp  # Return the valid temperature input
        except ValueError:
            # If the input is not a valid number, display an error message
            print("Invalid input! Please enter a valid numerical value for the temperature.")

# Function to get the conversion type
def get_conversion_type():
    while True:
        # Prompt the user to choose a conversion type
        conv_type = input("\nSelect conversion type:\n    1. Celsius to Fahrenheit\n    2. Fahrenheit to Celsius\nEnter 1 or 2: ")
        if conv_type in ['1', '2']:
            return conv_type  # Return the valid conversion type (1 or 2)
        else:
            # If the input is invalid, ask again
            print("Invalid input! Please enter 1 or 2.")

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# Main
temp = get_temperature()  # Get the temperature input from the user
conv_type = get_conversion_type()  # Get the desired conversion type

# If the user chose '1', convert from Celsius to Fahrenheit
if conv_type == '1':
    conv_temp = celsius_to_fahrenheit(temp)
    print(f"\n{temp} °C to Fahrenheit: {conv_temp:.2f} °F")

# If the user chose '2', convert from Fahrenheit to Celsius
elif conv_type == '2':
    conv_temp = fahrenheit_to_celsius(temp)
    print(f"\n{temp} °F to Celsius: {conv_temp:.2f} °C")


