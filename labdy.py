

test = lambda x: x * 2

print((lambda x: x * 2)(4))

my_list = [2, 14, 22, 7, 6, 4, 5, 17]

my_filter_list = list(filter(lambda x: x % 2 == 0, my_list))
print(my_filter_list)