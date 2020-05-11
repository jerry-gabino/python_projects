import statistics
# the filter() method filters the given
# iterable with the help of a function that tests
# each element against the condition passed into that
#    filter(function, iterable

my_list = [7, 5, 2, 8, 10, 73, 92]


def func(elem):
    if elem % 2 == 0:
        return True
    else:
        return False


output = filter(func, my_list)
print(list(output))


# using lambda function; inline function
output2 = filter(lambda elem: elem % 2 == 0, my_list)
print(list(output2))

# filter scores above average

score = [12, 20, 44, 77, 56, 88]
# finding average using statistics.mean(score)
average_val = statistics.mean(score)
print(average_val)
res = filter(lambda a: a > average_val, score)
print(list(res))
