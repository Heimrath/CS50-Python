print("Hello, world!")

#   ????????
# input("What is your name?")
# print("Hello, Matheus!")

# Looks better
name = input("What is your name? ")
print("Hello, " + name)

# Overriding the default end of print
print("Hello, ", end="")
print(name)

# Overriding the default separator of print
print("Hello, ", name, sep="")

# Another way to concatenate strings
print(f"Hello, {name}")