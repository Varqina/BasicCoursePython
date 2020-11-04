"""Create program to sum all digits from 0 to provided digit"""
import time


def sum_till(range_number_int):
    sum = 0
    for digit in range(range_number_int + 1):
        sum += digit
    return sum


def sum_till_generator_list(range_number_int):
    return sum([digit
                for digit in range(range_number_int + 1)
                ])


def sum_till_generator(range_number_int):
    return sum((digit
                for digit in range(range_number_int + 1)
                ))


def sum_till_generator_set(range_number_int):
    return sum({digit
                for digit in range(range_number_int + 1)
                })


def sum_till_value(range_number_int):
    return (1 + range_number_int) / 2 * range_number_int


def function_performance(function, value):
    start = time.perf_counter()
    function(value)
    end = time.perf_counter()
    function_name = str(function)
    function_name = function_name.replace("<function "," ")
    function_name = function_name[0: len(function_name)-15]
    print(function_name + ": " + str(end - start))

data = 10000000
function_performance(sum_till, data)
function_performance(sum_till_generator_list, data)
function_performance(sum_till_generator_set, data)
function_performance(sum_till_generator, data)
function_performance(sum_till_value, data)
