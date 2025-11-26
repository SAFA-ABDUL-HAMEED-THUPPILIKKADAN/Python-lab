list1 = ["name", "age"]

list2 = ["safa", 23]


mergeddict = {}

for i in range(len(list1)):
    mergeddict[list1[i]] = list2[i]


print(mergeddict)
