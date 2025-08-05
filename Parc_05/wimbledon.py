"""
Wimbledon
Estimate: 25 minutes
Actual: 20 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    data = read_wimbledon_data(FILENAME)
    champions = count_wins(data)
    countries = get_countries(data)

    print("Wimbledon Champions:")
    for name, count in champions.items():
        print(f"{name} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def read_wimbledon_data(filename):
    """Read Wimbledon data from CSV file and return a list of [Champion, Country]."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)
        data = []
        for line in in_file:
            parts = line.strip().split(",")
            champion = parts[2]
            country = parts[1]
            data.append([champion, country])
        return data


def count_wins(data):
    """Count how many times each champion has won. Return a dictionary."""
    champions_to_wins = {}
    for name, _ in data:
        champions_to_wins[name] = champions_to_wins.get(name, 0) + 1
    return champions_to_wins


def get_countries(data):
    """Return a set of unique countries from the data."""
    return {country for _, country in data}


if __name__ == "__main__":
    main()
