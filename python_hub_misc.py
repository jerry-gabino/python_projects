# What is the following output
myList = (1, 2, 3, 4, 5)
myList[0] = 10
for x in myList:
    print(x)
# TypeError: 'tuple' object does not support item assignment
# Replace Tuple with List to work properly