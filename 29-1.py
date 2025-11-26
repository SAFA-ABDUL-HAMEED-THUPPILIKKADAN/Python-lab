

import csv

Game_numbers = []

with open("sample4.csv", "r") as f1:
    read = csv.reader(f1)

    for row in read:
        Game_numbers.append(row[0])

print(Game_numbers[1::])
