"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    If the user inputs something that is not an integer, like "ten" or "3.14".
2. When will a ZeroDivisionError occur?
    If the user enters 0 as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Yes, by adding a while loop to make sure the denominator is not 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter a non-zero denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
