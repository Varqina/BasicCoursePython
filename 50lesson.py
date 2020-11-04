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


range_value = 100000
set_container = {i for i in range(range_value)}

def set_function(range_value):
    set_container = {i for i in range(range_value)}
    #set_30 = {30}
    #set_30.issubset(set_container)

list_container = [i for i in range(range_value)]
def list_function(range_value):
    list_container = [i for i in range(range_value)]
    #list_container.count(30)

def sum_till_value(range_number_int):
    return (1 + range_number_int) / 2 * range_number_int


def function_performance(function, value=None, iteration_number=0):
    start = time.perf_counter()
    for i in range(iteration_number):
        function(value)
    end = time.perf_counter()
    function_name = str(function)
    function_name = function_name.replace("<function ", " ")
    function_name = function_name[0: len(function_name) - 15]
    print(function_name + ": " + str(end - start))


# data = 10000000
# function_performance(sum_till, data)
# function_performance(sum_till_generator_list, data)
# function_performance(sum_till_generator_set, data)
# function_performance(sum_till_generator, data)
# function_performance(sum_till_value, data)
function_performance(set_function, value=100000, iteration_number=1000)
#add set is slover than list
#find ser element is faster than list
function_performance(list_function, value=100000, iteration_number=1000)
