
"""Let's find all values from range 100 to 470 and make them divided by 7 but not 5"""

result_list = [
    digit
    for digit in range(100, 471)
    if digit % 7 == 0
    if digit % 5 != 0
]
print("Result list = " + str(result_list))
result_set = {
    digit
    for digit in range(100, 471)
    if digit % 7 == 0
    if digit % 5 != 0
}

print("Result set = " + str(result_set))
result_dictionary_generator = (
    digit
    for digit in range(100, 471)
    if digit % 7 == 0
    if digit % 5 != 0
)

iteration = 1
result_dictionary = {}
for element in result_dictionary_generator:
    result_dictionary[iteration] = element
    iteration += 1

print(result_dictionary)

result_generator = (
    digit
    for digit in range(100, 471)
    if digit % 7 == 0
    if digit % 5 != 0
)
result_generator_list = []
for digit in result_generator:
    result_generator_list.append(digit)

print(result_generator_list)

if len(result_dictionary) == len(result_list):
    print("True")