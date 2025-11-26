str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

merged_list = []

# find the smaller length
min_len = min(len(str1), len(str2))

# merge alternately
for i in range(min_len):
    merged_list.append(str1[i])
    merged_list.append(str2[i])

# add remaining characters from the longer string
if len(str1) > len(str2):
    merged_list.extend(str1[min_len:])
else:
    merged_list.extend(str2[min_len:])

# print the merged list
for ch in merged_list:
    print(ch)
