"""
Emails
Estimate: 20 minutes
Actual: 10 minutes
"""

def extract_name_from_email(email):
    """Extract and format name from email (before the @)."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


def main():
    """Main program to collect emails and associated names."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email:
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ('', 'y'):
            name = input("Name: ").strip()
        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
