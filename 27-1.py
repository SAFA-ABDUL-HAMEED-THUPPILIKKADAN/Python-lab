with open("input1.txt", "r") as infile:
    lines = infile.readlines()

with open("output2.txt", "w") as outfile:
    outfile.writelines(lines[2::3])
