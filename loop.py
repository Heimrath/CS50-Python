i = 0
while i < 3:
    print("meow")
    i += 1

for i in range(3):
    print("auau")


while True:
    n = int(input("Enter a positive number: "))
    if(n > 0):
        break
    else:
        continue

for _ in range(n):
    print("meow")