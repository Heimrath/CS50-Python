import csv

name = input("Qual seu nome? ")
home = input("Qual sua casa? ")

with open("writing.csv", "a", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
    