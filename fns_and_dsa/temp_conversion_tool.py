FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

temp_to_convert = float(input("Enter the temperature to convert: "))
# if type(temp_to_convert) == str:
#     print('Invalid temperature. Please enter a numeric value.')
#     pass

C_or_F = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()


def convert_to_fahrenheit(celsius):
    celsius = temp_to_convert
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit}°F")


def convert_to_celsius(fahrenheit):
    fahrenheit = temp_to_convert
    celsius = ((fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR)
    print(f"{fahrenheit}°F is {celsius}°C")


if C_or_F == "C":
    convert_to_fahrenheit(temp_to_convert)
elif C_or_F == "F":
    convert_to_celsius(temp_to_convert)

