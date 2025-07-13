"""Guitar program to load, add, and save guitars."""

from guitar import Guitar
import csv

FILENAME = "guitars.csv"

def main():
    """Main function to manage guitar inventory."""
    guitars = load_guitars(FILENAME)

    print("These are the current guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

    print("\nAdd new guitars:")
    name = input("Name: ")
    while name != "":
        year = get_valid_int("Year: ")
        cost = get_valid_float("Cost: ")
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")

        guitars.sort()
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, "r") as in_file:
            reader = csv.reader(in_file)
            for row in reader:
                name, year, cost = row
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"Warning: '{filename}' not found. Starting with an empty list.")
    return guitars

def get_valid_int(prompt):
    """Get a valid integer from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input; enter a valid number.")


def get_valid_float(prompt):
    """Get a valid float from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input; enter a valid number.")


if __name__ == '__main__':
    main()

