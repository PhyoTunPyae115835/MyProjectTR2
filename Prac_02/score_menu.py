"""
score_menu.py
Program that uses a menu to get a score, print the result, and show stars.
"""


def main():

    score = get_valid_score()
    menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell!")

def get_valid_score():
    """Get a score from the user between 0 and 100 inclusive."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def determine_result(score):
    """Return result string based on the score."""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def print_stars(score):
    """Print stars equal to the score (as int)."""

    print("*" * int(score))

main()