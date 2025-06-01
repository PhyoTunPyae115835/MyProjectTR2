"""
score.py
Program that rates user and random scores using a function.
"""

import random

def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(f"Your result is: {result}")

    random_score = random.uniform(0, 100)
    print(f"Random score is {random_score:.2f}, result: {determine_result(random_score)}")


def determine_result(score):
    """Return the result string based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
