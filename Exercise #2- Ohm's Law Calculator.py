# Function to get user choice for calculation
def get_vir():
    while True:
        vir = input("\nWhat do you want to calculate? \n  1. Voltage\n  2. Current\n  3. Resistance\nEnter 1, 2, or 3: ")
        if vir in ['1', '2', '3']:
            return vir
        else:
            print("Invalid input! Please select 1, 2, or 3.")

# Function to get numerical input from the user
def get_numerical_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid numerical value.")

# Function to calculate voltage (V = I * R)
def calculate_voltage():
    current_input = get_numerical_input("\nEnter the value of current (in ampere): ")
    resistance_input = get_numerical_input("Enter the value of resistance (in ohm): ")
    result = current_input * resistance_input
    print(f"\nValue of Voltage: {result:.2f} V")

# Function to calculate current (I = V / R)
def calculate_current():
    voltage_input = get_numerical_input("\nEnter the value of voltage (in volt): ")
    while True:
        resistance_input = get_numerical_input("Enter the value of resistance (in ohm): ")
        if resistance_input == 0:
            print("Error! Resistance cannot be zero. Please enter a valid value.")
        else:
            result = voltage_input / resistance_input
            print(f"\nValue of Current: {result:.2f} A")
            break

# Function to calculate resistance (R = V / I)
def calculate_resistance():
    voltage_input = get_numerical_input("\nEnter the value of voltage (in volt): ")
    while True:
        current_input = get_numerical_input("Enter the value of current (in ampere): ")
        if current_input == 0:
            print("Error! Current cannot be zero. Please enter a valid value.")
        else:
            result = voltage_input / current_input
            print(f"\nValue of Resistance: {result:.2f} Ω")
            break

# Main
vir = get_vir()
# Call appropriate calculation function based on choice
if vir == "1":
    calculate_voltage()
elif vir == "2":
    calculate_current()
elif vir == "3":
    calculate_resistance()
