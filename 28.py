import csv

with open("sample4.csv", "r", newline="") as f1:
    read = csv.reader(f1)

    for row in read:
        print(row)
