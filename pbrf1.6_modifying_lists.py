#we can change the value of an element in a list below by appending the position to equal a new value of the item, run it!
garden = ["beans", "peppers", "tomatoes", "onions", "basil"]
print(garden)

garden[0] = "eggplant"
print(garden)

#you can add append an element on the list by using ".append" statement on the list, run it!
colors = ["red", "white", "yellow", "green", "blue"]
print(colors)

colors.append("purple")
print(colors)

#an empty list can be appended and built with ".append" statement and the element name.
wood = []
wood.append("beech")
wood.append("cherry")
wood.append("oak")
wood.append("pine")
print(wood)

#you can add an element in a list with ".insert" statement.
soda = ["Pepsi", "Dr. Pepper", "Coke", "Sprite"]
print(soda)

soda = ["Pepsi", "Dr. Pepper", "Coke", "Sprite"]
soda.insert(4, "Mr. Pibb")
print(soda)

#deleting an element in a list is done by using the "del" statement and position on the list.
metal = ["iron", "steel", "bronze", "tin", "copper"]
print(metal)

del metal[2]
print(metal)