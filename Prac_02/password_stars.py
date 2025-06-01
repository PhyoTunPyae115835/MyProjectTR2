"""
Program to prompt the user for a password and display asterisks
matching the length of the password.
"""

def main():
    password = get_password()
    print('*' * len(password))


def get_password():
    """Prompt the user to enter a password and return it."""
    return input("Enter password: ")

def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print('*' * len(password))


main()
