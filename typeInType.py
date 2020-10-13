name = "Piotr"
age = 28

name2 = "Radoslaw"
age2 = 26

person1 = ('Piotr', 28)
person2 = ("Radoslaw", 26)

personList = [
    ['Piotr', 29],
    ['Radoslaw', 26]
]
tuplelist = [
    (2, 4, 4, "Tomek"),
    (3, 4, 5, "Asia")
]

print(personList[1][1])
print(personList[1])
print(tuplelist[0][3])
tuplelist.append((2, 2, 2, "Karol"))
print(tuplelist)

for value1, value2 in personList:
    print(value1)
    print(value2)
    print(str(value1)+str(value2))