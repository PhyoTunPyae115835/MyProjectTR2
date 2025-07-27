"""
CP1404/CP5632 Practical
Taxi simulator
"""

def main():
    """Start taxi simulator with just a menu."""
    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            print("Choose taxi - not implemented yet")
        elif choice == "d":
            print("Drive - not implemented yet")
        else:
            print("Invalid option")

        print(menu)
        choice = input(">>> ").lower()

    print("Thank you for using the taxi simulator.")


if __name__ == "__main__":
    main()
