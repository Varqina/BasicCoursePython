"""
Only one value
No order



"""

A = {20, 21, 44, 55, 66, 66}
list = [22, 33, 44, "AAA"]
print(A)
A.add("seven")
print(A)
setList=set(list)
print(setList)

print(A&setList) #has the same value
print(A|setList) #has all values
print(A-setList) #remove from A set
print(setList-A) #remove from set A
print(A^setList) #XOR
#A.discard("remove element, no issue if there is no value")
#A.remove("remove element, issue if no value")

B={66, 44, 'seven'}
print(A.issubset(setList))
print(B.issubset(A))