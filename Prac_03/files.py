# 1. Ask user for name and write it to name.txt
name = input("Enter your name: ")
file_out = open("name.txt", "w")
file_out.write(name)
file_out.close()

# 2. Read the name from name.txt and print a greeting
file_in = open("name.txt", "r")
saved_name = file_in.read().strip()
file_in.close()
print(f"Hi {saved_name}!")

# 3. Read the first two numbers from numbers.txt, add them and print the result
with open("numbers.txt", "r") as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
    print(number1 + number2)  # Should print 59

# 4. Sum all numbers in numbers.txt and print the total
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line)
    print(total)
