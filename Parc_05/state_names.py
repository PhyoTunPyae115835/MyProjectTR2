"""
CP1404/CP5632 Practical
State names in a dictionary
Formatted using PEP 8 and EAFP style
"""

STATE_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# 1. Print all states and names, neatly aligned
for code, name in STATE_NAMES.items():
    print(f"{code:3} is {name}")

# 2. Get user input and use EAFP (try/except), no while True used
state_code = input("Enter short state: ").strip().upper()
while state_code:
    try:
        print(f"{state_code} is {STATE_NAMES[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").strip().upper()
