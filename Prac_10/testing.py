"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from Prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase as a sentence:
    Capitalize first letter and end with a single full stop.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("it is an ex parrot")
    'It is an ex parrot.'
    >>> format_sentence("already correct.")
    'Already correct.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:]


def run_tests():
    """Run the tests on the functions."""
    # repeat_string() assertions
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Car class assertions
    car = Car()
    assert car.odometer == 0, "Car does not set odometer correctly"

    car = Car(fuel=10)
    assert car.fuel == 10, "Car fuel not set correctly with argument"

    car_default = Car()
    assert car_default.fuel == 0, "Car default fuel should be 0"


run_tests()
doctest.testmod()
