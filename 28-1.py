import csv

with open("sample4.csv", "r") as f1:
    read = csv.DictReader(f1)

    for row in read:
        if int(row[' "Game Length"']) > 30:
            print(row[' "Game Length"'])
