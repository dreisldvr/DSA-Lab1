# Exercise 2: Ohm’s Law Calculator
# Instructions:
# 1.	Ask the user what they want to calculate: Voltage, Current, or Resistance.
# 2.	Based on their choice, prompt the user to input the appropriate values.
# 3.	Use Ohm's Law to calculate the missing variable and display the result.
# 4.	Handle cases where division by zero might occur.


def get_vir():
    while True:
        vir = input("\nWhat do you want to calculate? \n  1. Voltage\n  2. Current\n  3. Resistance\nEnter 1, 2, or 3: ")
        if vir in ['1', '2', '3']:
            return vir
        else:
            print("Invalid input! Please select 1, 2, or 3.")

def get_numerical_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid numerical value.")

def calculate_voltage():
    current_input = get_numerical_input("\nEnter the value of current (in ampere): ")
    resistance_input = get_numerical_input("Enter the value of resistance (in ohm): ")
    result = current_input * resistance_input
    print(f"\nValue of Voltage: {result:.2f} V")

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


vir = get_vir()

if vir == "1":
    calculate_voltage()
elif vir == "2":
    calculate_current()
elif vir == "3":
    calculate_resistance()
