"""
A series of for-loop demonstrating:
Printing odd numbers
Counting in steps
Printing repeated characters
"""

# 1. Display odd numbers between 1 and 20
print("1. Odd numbers from 1 to 20:")
for i in range(1, 21, 2):
    print(i, end=' ')
print("\n")  # newline

# a. Count in 10s from 0 to 100
print("a. Count in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print("\n")

# b. Count down from 20 to 1
print("b. Count down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print("\n")

# c. Print n stars on one line
print("c. Print n stars in one line:")
n = int(input("Number of stars: "))
print("*" * n)
print()  # optional spacing

# d. Print lines of increasing stars
print("d. Increasing lines of stars:")
for i in range(1, n + 1):
    print("*" * i)
