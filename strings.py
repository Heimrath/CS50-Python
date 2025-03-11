name = input("What is your name? ")
print(f"Hello, {name}")

# Remove whitespace from String
name = name.strip()
print(f"Hello, {name}")

# Capitalize the first letter of the string
name = name.capitalize()
print(f"Hello, {name}")

# Capitalize the first letter of each word in the string
name = name.title()
print(f"Hello, {name}") 

# Remove whitespace and capitalize the first letter of each word in the string
name = name.strip().title()
print(f"Hello, {name}")

# All together
fullName = input("What is your full-name? ").strip().title()
print(f"Hello, {fullName}")

# Split user's name into first and last name
first, last = fullName.split(" ")

print(f"Hello, {fullName}")
print(f"Hello, {first}")
print(f"Hello, {last}")