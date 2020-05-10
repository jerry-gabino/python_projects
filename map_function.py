# define my list
my_list = [12, 13, 14, 15]


# define function
def func(elem):
    return elem ** 2


# map() function applies given function to each
# element of an iterable set

square = map(func, my_list)

# show list of numbers
for i in my_list:
    print(i)

# using lambda function; inline function
square2 = list(map(lambda elem: elem ** 2, my_list))
print(square2)

# print the square using the map() function
print(list(square))

# use map and lambda functions to add corresponding items of two lists
list_1 = [12, 9, 8]
list_2 = [10, 5, 4]

output = list(map(lambda n1, n2: n1 + n2, list_1, list_2 ))
print(output)