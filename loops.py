"""


While
For

"""

number = 5
while number >= 0:
    print("loop while")
    number -= 1

while number < 10:
    print("second loop")
    number += 1
    if number == 9:
        print("The last")

for i in [0,1,2]:
    print(i)

for i in [1,4,8]:
    print(i)

for i in range(10):
    print("loop for")