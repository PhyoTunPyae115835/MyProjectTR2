"""
Guitar program to load, display, and manage guitars.
"""

from guitar import Guitar
import csv

def main():
    """Main function to load, sort, and display guitars."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    # Sort guitars by year
    guitars.sort()

    display_guitars(guitars)

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

if __name__ == "__main__":
    main()
