"""
Menu-driven program that greets or farewells the user by name.
"""

# Get user name
name = input("Enter name: ")

# Define the menu display
menu = "\n(H)ello\n(G)oodbye\n(Q)uit"

# Display menu and get initial choice
print(menu)
choice = input(">>> ").upper()

# Loop until user chooses to quit
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Redisplay menu and get next choice
    print(menu)
    choice = input(">>> ").upper()

print("Finished.")
