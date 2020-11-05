#**args
#*arg



def test_arguments(*args):
    print(sum(args))



test_arguments(2,2,2,2,2,2)

def test_arguments_2(**args):
    for element in args:
        print(args[element])

test_arguments_2(amazon="ebay")