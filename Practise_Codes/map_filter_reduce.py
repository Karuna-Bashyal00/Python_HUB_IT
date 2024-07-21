
# note: Map Function 
# ! Program to calculate square of a number in a iterable list

# def square(x):
#     return x*x

# numbers = [1,2,3,4,5]

# ?map (function, iterable)
# final_square = map(square, numbers)

# print(final_square)

# note: Map Function Using Lambda
# numbers = [1,2,3,4,5]

# final_square = map(lambda x: x*2, numbers)
# print(list(final_square))

# note: Filter Function
# ! Program to calculate even numbers from a list

# def is_even(x):
#     return x % 2 == 0

# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = filter(is_even, numbers)
# print(list(even_numbers))

# note: Filter Function Using Lambda
# numbers = [1,2,3,4,5,6,7,8,9,10]
# odd_numbers = filter(lambda x:x%2 != 0, numbers)
# print(list(odd_numbers))

# note: Reduce Function
# ! Program to calculate sum of numbers from a list

# from functools import reduce

# def sum_numbers(x,y):
#     return x + y

# numbers = [1,2,3,4,5]
# total_sum = reduce(sum_numbers, numbers)
# print(total_sum)

# ! Program to calculate minimum value from a list
# from functools import reduce

# numbers = [1,2,3,4,5]
# def min_number(x,y):
#     return x if x<y else y

# min_value = reduce(min_number, numbers)
# print(min_value)

# ! Program to calculate minimum value using lambda
from functools import reduce

numbers = [1,2,3,4,5]
min_value = reduce(lambda x,y: x if x<y else y, numbers)
print(min_value)




