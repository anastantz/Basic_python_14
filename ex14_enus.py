# Program that converts a temperature from Celsius to Fahrenheit

celsius = float(input("Enter the temperature in °C: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"The temperature of {celsius:.1f}°C corresponds to {fahrenheit:.1f}°F.")