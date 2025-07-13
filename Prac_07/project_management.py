from project import Project
from datetime import datetime

FILENAME = "projects.txt"

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = """
- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""

    while True:
        print(menu)
        choice = input(">>> ").lower()

        if choice == "l":
            filename = input("Filename to load: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "s":
            filename = input("Filename to save: ")
            save_projects(filename, projects)
            print(f"Projects saved to {filename}")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            new_project = add_new_project()
            projects.append(new_project)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            confirm = input(f"Would you like to save to {FILENAME}? ").lower()
            if confirm == "yes":
                save_projects(FILENAME, projects)
                print(f"Projects saved to {FILENAME}")
            else:
                print("Changes not saved.")
            break
        else:
            print("Invalid option")


def load_projects(filename):
    """Load projects from a file into a list of Project objects."""
    projects = []
    with open(filename, "r") as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            name, start_date, priority, cost_estimate, completion_percentage = parts
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects

def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete_projects = [p for p in projects if not p.is_complete()]
    complete_projects = [p for p in projects if p.is_complete()]

    incomplete_projects.sort()
    complete_projects.sort()

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete_projects:
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Filter and display projects that start on or after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")
        return

    filtered_projects = [p for p in projects if p.start_date >= filter_date]
    filtered_projects.sort(key=lambda p: p.start_date)

    print(f"Projects starting on or after {filter_date.strftime('%d/%m/%Y')}:")
    for project in filtered_projects:
        print(f"  {project}")

def add_new_project():
    """Prompt user to enter new project details and return a Project object."""
    print("Let's add a new project")
    name = input("Name: ")
    while True:
        try:
            start_date_str = input("Start date (dd/mm/yyyy): ")
            datetime.strptime(start_date_str, "%d/%m/%Y")  # Validate format
            break
        except ValueError:
            print("Invalid date format. Use dd/mm/yyyy.")

    priority = get_valid_int("Priority: ")
    cost_estimate = get_valid_float("Cost estimate: $")
    completion = get_valid_int("Percent complete: ", min_value=0, max_value=100)

    return Project(name, start_date_str, priority, cost_estimate, completion)


def get_valid_int(prompt, min_value=None, max_value=None):
    """Get a validated integer input from the user."""
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Value must be between {min_value} and {max_value}")
                continue
            return value
        except ValueError:
            print("Invalid input; enter an integer.")


def get_valid_float(prompt):
    """Get a validated float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input; enter a number.")

if __name__ == "__main__":
    main()