"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from Prac_06.car import Car


def main():
    """Demo test code to show how to use Car class with name and methods."""
    # Create a limo car with 100 units of fuel
    limo = Car("Limo", 100)

    # Add 20 more units of fuel
    limo.add_fuel(20)

    # Print current fuel and full object
    print(f"Fuel in limo: {limo.fuel}")
    print(limo)

    # Attempt to drive 115 km
    limo.drive(115)

    # Print updated state
    print(limo)


main()