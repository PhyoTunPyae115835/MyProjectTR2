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