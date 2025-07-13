"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        """Return a formatted string representation of the ProgrammingLanguage."""
        return (f"{self.name}, Typing={self.typing}, Reflection={self.reflection}, "
                f"Year={self.year}, Pointer Arithmetic={self.pointer_arithmetic}")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"



def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, True)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, False)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, False)

    languages = [ruby, python, visual_basic]

    # Test __str__ output
    for language in languages:
        print(language)

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()

