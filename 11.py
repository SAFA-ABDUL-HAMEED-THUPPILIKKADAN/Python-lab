string = input("enter a string :")
arr = list(string)

length = len(arr)

first = arr[0]
last = arr[length-1]


arr[0] = last
arr[length-1] = first


str = ''.join(arr)

print(str)
