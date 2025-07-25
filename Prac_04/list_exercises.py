"""
List operations and username security checker
"""

def main():
    # Part 1: Basic list operations
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

    # Part 2: Username check
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45']
    user_input = input("\nUsername: ")
    if user_input in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()
