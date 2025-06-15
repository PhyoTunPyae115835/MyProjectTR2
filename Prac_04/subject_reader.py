"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Main function to load and display subject data."""
    subjects = load_data()
    display_subjects(subjects)


def load_data():
    """Read subject data from file and return a list of [subject, lecturer, number]."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            parts = line.strip().split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data


def display_subjects(subjects):
    """Display formatted subject details."""
    for subject_code, lecturer, student_count in subjects:
        print(f"{subject_code} is taught by {lecturer} and has {student_count:3} students")


if __name__ == "__main__":
    main()
