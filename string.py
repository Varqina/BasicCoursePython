name = "Piotr"
surname = "Flis"
#print(name +" "+ surname)

longString = "aaaaaaaaa\
bbbbbbbbbbb\
000ccccccccccc\
kkkkkk"

anotherLongString = """
a
1
2
"""
#print(name[0]) #return P
#print(name[-1]) # returns last r
#print(name[:])# returns all
#print(name[1:])# return all started from index 1
#print(name[1:3])#return characters 1 and 2

#Capitalize- first captialized other small
#print(name.capitalize()) #Piotr

#CaseFold - used as lower to characters not specified to natural alphabet
#print(name.casefold())#ß'; casefold() converts it to "ss".

#Center - it makes string long as paremeter and blank value is filled with characters, space default
#print(name.center(10,"$")) $$Piotr$$$

#count - how many times substring is in main string
#print(name.count(surname))

#Upper all characters up
#print(name.upper())
#todo
#Book with python and check all string!