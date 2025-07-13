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

if __name__ == '__main__':
    main()

