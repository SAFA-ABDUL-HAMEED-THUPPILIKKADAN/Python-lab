import csv


data = [
    {"name": "safa", "age": 23},
    {"name": "sana", "age": 21},
    {"name": "sara", "age": 25},
]

filename = "output4.csv"

fieldnames = ["name", "age"]


with open(filename, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames)

    writer.writeheader()
    writer.writerows(data)
