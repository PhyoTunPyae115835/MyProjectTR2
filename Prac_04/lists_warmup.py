"""CP1404/CP5632 Practical - List warm-up"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# Predictions:
# numbers[0] -> 3
# numbers[-1] -> 2
# numbers[3] -> 1
# numbers[-1] -> 2
# numbers[3:4] -> [1]
# 5 in numbers -> True
# 7 in numbers -> False
# "3" in numbers -> False
# numbers + [6, 5, 3] -> [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# List changes
numbers[0] = "ten"
numbers[-1] = 1

# Slice and check
print(numbers[2:])      # Print from 3rd element onward
print(9 in numbers)     # Check if 9 is in the list
