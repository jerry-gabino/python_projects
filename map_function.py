# define my list
my_list = [12, 13, 14, 15]


# define function
def func(elem):
    return elem ** 2


# map() applies function to each element of an iterable set
square = map(func, my_list)

# show list of numbers
for i in my_list:
    print(i)

# print the square using the map() function
print(list(square))
