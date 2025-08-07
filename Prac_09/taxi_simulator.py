"""
CP1404/CP5632 Practical
Taxi simulator
"""

from Prac_09.taxi import Taxi
from Prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>> ").lower()

    while choice != 'q':
        if choice == 'c':
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            current_taxi = taxis[get_valid_index("Choose taxi: ", taxis)]
            print(f"Selected: {current_taxi}")

        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi first.")
            else:
                distance = get_positive_int("Drive how far? ")
                current_taxi.start_fare()
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print(f"Your trip cost you ${fare:.2f}")
                total_bill += fare

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_index(prompt, items):
    """Get a valid index from user input."""
    while True:
        try:
            index = int(input(prompt))
            if 0 <= index < len(items):
                return index
            print("Invalid taxi choice")
        except ValueError:
            print("Invalid input; enter a number")


def get_positive_int(prompt):
    """Get a positive integer from user input."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Distance must be > 0")
        except ValueError:
            print("Invalid input; enter a number")


if __name__ == "__main__":
    main()
