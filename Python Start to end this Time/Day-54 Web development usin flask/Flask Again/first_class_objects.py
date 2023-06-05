#
# def add(n1, n2):
#     return n1 + n2
#
# def sub(n1, n2):
#     return n1 - n2
#
# def mul(n1, n2):
#     return n1 * n2
#
# def div(n1, n2):
#     return n1 / n2
#
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# result = calculate(mul, 4, 5)
# print(result)
#
#
# def outer_function():
#     print("I am outer function")
#     def inner_function():
#         print("I am inner function")
#
#     return inner_function
#
#
# result = outer_function()
#
# result()
#


# ############## Python Decorators ################
# import time
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(5)
#         function()
#     return wrapper_function
#
#
# @delay_decorator
# def say_hello():
#     print(f"Hello there!")
#
# @delay_decorator
# def say_bye():
#     print(f"Good Bye!")
#
#
# say_hello()
# say_bye()

import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function



@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i *= i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i *= i


fast_function()
slow_function()




