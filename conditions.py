"""
>
<
==
!=
>=
<=
"""
a = 5
b = 5
print(5 > 4) # returns true
if a > b:
    print("True")
elif a == b:
    print ("Elif")
elif a ==5:
    print("a = 5")
else:
    print("else")

"""
and
True True - True
True False - False
False True - False
False Fasle - False

or
True True - True
True False - True
False True - True
False False - False

not makes opposite value

"""

if True and True:
    print ("1 - True")
if False or False:
    print ("2 - True")
else:
    print("2 - False")

if not False and True:
    print ("not True")