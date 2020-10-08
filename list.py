"""
len lenght of the list
append add object on the end of the list (list in list)
extend extend list with other list/objects
insert add object on specify index
index return number of index
sort (reverse) sorting
max, min returns max and min value
count how many times sth appeared
pop remove last element from the list
remove, remove first existence of object
clear, clear whole list
"""


#list starts from 0
listOfName = ["Piotr", "Radek", "Miro"]
listOfDigits = [1,22,3]
listMixed = ["Perla", 15, 12, "Sara"]

# for name in listOfName:
#     print(name)
# print(listOfName[1])
# print(listOfName[-1])
# listOfName[-1] = "Basia"
# print(listOfName[-1])
# print(listOfName)
#
# print("Piotr" in listOfName)
# print("Piotr" in listMixed)

maxlist = listMixed + listOfName + listOfDigits

print(maxlist)
print(len(maxlist))
maxlist.append(1)
maxlist.append(listOfName)
print(maxlist)
maxlist.extend(listOfDigits)
print(maxlist)
maxlist.insert(0,"ja")
#change value list in list
print(maxlist)
#Doesn't work why?
#print(listMixed.index(1))
#print(maxlist.sort())
print(listOfDigits)
listOfDigits.sort()
print(listOfDigits)

#to test max,min for list with names
#to test list with strings and sort