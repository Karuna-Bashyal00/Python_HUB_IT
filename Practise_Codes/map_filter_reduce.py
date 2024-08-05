
# note: Map Function 
# ! Program to calculate square of a number in a iterable list

# numbers = [1,2,3,4,5]

# def square(x):
#     return x * x

# final_square = map(square,numbers)

# print(list(final_square))

# ?map (function, iterable)


# note: Map Function Using Lambda
# numbers = [1,2,3,4,5]

# final_square = map(lambda x: x*2, numbers)
# print(list(final_square))

# note: Filter Function
# ! Program to calculate even numbers from a list

# numbers = [2,3,4,5,6,7,8,9,10]

# def even_number(x):
#     return x if x%2 == 0 else None

# check_even = filter(even_number, numbers)

# print(tuple(check_even))

# note: Filter Function Using Lambda
# numbers = [1,2,3,4,5,6,7,8,9,10]
# odd_numbers = filter(lambda x:x%2 != 0, numbers)
# print(list(odd_numbers))

# note: Reduce Function
# ! Program to calculate sum of numbers from a list

# from functools import reduce

# numbers = [1,2,3,4,5]

# def sum_numbers(x,y):
#     return x + y

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
# from functools import reduce

# numbers = [1,2,3,4,5]
# min_value = reduce(lambda x,y: x if x<y else y, numbers)
# print(min_value)

from functools import reduce

numbers = [1,2,3,4,5]

def square(x):
    return x*x

def addition(x,y):
    return x+y

final_square = list(map(square, numbers))

reduced_sum = reduce(addition, final_square)

print(f"Sum Of Squared Numbers:", reduced_sum)


