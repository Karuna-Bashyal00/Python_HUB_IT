
# note: Simple Generator example
# def generats():
#     yield 1
#     yield 2
#     yield 3

# gen = generats()
# print(next(gen))
# print(next(gen))
# print(next(gen))

# note: Fibonacci Series using Generator
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b

# fib = fibonacci()
# for _ in range(10):
#     print(next(fib))

# note: Generator Expression without yield
# ?simple expression i.e List Comprehension
# square_list = [x**2 for x in range(5)]

# ?Generator Expression
# square_gen = (x**2 for x in range(5))

# ?printing list
# print(square_list)

# ?printing generator
# print(square_gen)

# ?iterating expression for generator
# for _ in square_gen:
#     print(_)