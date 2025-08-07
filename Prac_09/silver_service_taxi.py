"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""

from Prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness and flagfall."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness  # override instance variable

    def get_fare(self):
        """Return the fare with flagfall included, rounded to nearest 10c."""
        return round(super().get_fare() + self.flagfall, 1)

    def __str__(self):
        """Return string representation with flagfall info."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
