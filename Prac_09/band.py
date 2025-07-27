"""
CP1404/CP5632 Practical
Band class using composition
"""

class Band:
    """Band class that contains multiple musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a Musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Tell each musician to play their instruments."""
        print(f"{self.name} band is playing:")
        for musician in self.musicians:
            musician.play()
