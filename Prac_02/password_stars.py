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


main()
