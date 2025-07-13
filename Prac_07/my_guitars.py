"""
Guitar program to load, display, and manage guitars.
"""

from guitar import Guitar
import csv

def main():
    """Main function to load, sort, and display guitars."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    # Add new guitars
    print("\nAdd new guitars:")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")
        name = input("Name: ")

    # Sort guitars by year
    guitars.sort()

    # Display all guitars
    print("\nThese are all the guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"{new_guitar} added.\n")

    display_guitars(guitars)
    # Save to CSV
    save_guitars(filename, guitars)

def load_guitars(filename):
    """Load guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, "r") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars."""
    print("These are the current guitars:")
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

def save_guitars(filename, guitars):
    """Save the list of guitars to a CSV file."""
    with open(filename, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

if __name__ == "__main__":
    main()
