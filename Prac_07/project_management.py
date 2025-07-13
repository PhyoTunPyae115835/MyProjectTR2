from project import Project

FILENAME = "projects.txt"

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
