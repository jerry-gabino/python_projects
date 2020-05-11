# The reduce() function accepts a function and a
# sequence and returns a single value calculated as follows"
# Initially the function is called with the first two
# items from the sequence and the results is returned.
# The function is then called again with the result obtained
# in step 1 and the next value of the sequence.  This process
# keeps repeating until there are items in the sequence
#    reduce(function, sequence[, initial])

# multiply elements fo a list (find factorial
from functools import reduce

my_list = [1, 2, 3, 4]
res = reduce(lambda n1, n2: n1 * n2, my_list)
print(res)

# add elements of a list
res = reduce(lambda n1, n2: n1 + n2, my_list)
print(res)
