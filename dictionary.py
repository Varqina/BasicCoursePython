"""
key - value
value, key can be mixed type

"""
#to check all functions
room = {49:'Piotr', 69:'Radoslaw'}
rooms = {22:"Radi", 22:"Piotr"}
roomstoto = {"two":"test", "key":"lock"}

print(room)
print(rooms)
print(roomstoto)
print(room)
room[33] = "test"
print(room)
rooms[22] = "RAdi"
print(rooms)

#add element

roomstoto[11]="Element"
print(roomstoto)

print(rooms.get(22))
rooms.update({400:"jas"})
print(rooms)
del(rooms[400])
print(rooms)
rooms.pop(22)
print(rooms)
room.popitem()
print(room)
print(len(room))