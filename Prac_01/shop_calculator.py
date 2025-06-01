"""
Calculates the total price for a number of items.
Applies a 10% discount if total is over $100.
"""

# Input validation loop
num_items = int(input("Number of items: "))
while num_items <= 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items: "))

# Get item prices
total_price = 0
for i in range(num_items):
    price = float(input(f"Price of item: "))
    total_price += price

# Apply discount if applicable
if total_price > 100:
    total_price *= 0.9  # Apply 10% discount

# Final output
print(f"Total price for {num_items} items is ${total_price:.2f}")
