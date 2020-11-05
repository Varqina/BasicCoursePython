#**args
#*arg



def test_arguments(*args):
    print(sum(args))



test_arguments(2,2,2,2,2,2)

def test_arguments_2(**args):
    for element in args:
        print(args[element])

test_arguments_2(amazon="ebay")



def copy_test(input_list):
    input_list[0] = 1
    #return input_list


test_list2 = [2,2,2]
test_list = [2,2,2]

print(copy_test(test_list))
print(test_list)

print(copy_test(test_list2.copy()))
print(test_list2)

