# list to Dictionary
fruits = ["apples", "bananas", "oranges"]

fruit_Dictionary = {k: v for k, v in enumerate(fruits)}
print(fruit_Dictionary)

# Tuples to Dictionary
letters = [(0, "a"), (1, "b"), (2, "c")]
letter_Dictionary = dict(letters)
print(letter_Dictionary)

# two lists
indicies = [0, 1, 2]
letters = ["a", "b", "c"]


zipped = zip(indicies, letters)
print(zipped)
letter_Dictionary = dict(zipped)
print(letter_Dictionary)

# default values
fruits = ["apples", "bananas", "oranges"]
fruit_Dictionary = dict.fromkeys(fruits, 0)
print(fruit_Dictionary)
