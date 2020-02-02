# two exact same functions with different sintax
def add(x, y):
    return x + y

add2 = lambda x, y : x + y

# lambda for interactive shell
# lambda in list methods that need a callback function: sorting, mapping and filtering

nums = [1,2,3]

def is_greater_than_one(x):
    return x > 1

more_than_one_nums = filter(is_greater_than_one, nums)
print(list(more_than_one_nums))

# using lambda instead:

more_than_one_nums = filter(lambda x: x > 1, [1,2,3])
print(list(more_than_one_nums))