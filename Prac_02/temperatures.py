"""
temperatures.py
Provides functions to convert Celsius to Fahrenheit and Fahrenheit to Celsius.
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def main():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Fahrenheit: {fahrenheit:.2f}")

    fahrenheit = float(input("Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"Celsius: {celsius:.2f}")


main()
