#we can use the ".sort()" statement to put a list in alphabetical order.
horses = [ "Appalosa", "Fresian", "Mustang", "Clydesdale", "Arabian" ]
horses.sort()
print(horses)

#we can also arrange our list in alphabetical order backwards with the ".sort(reverse=True)".
horses = [ "Appalosa", "Fresian", "Mustang", "Clydesdale", "Arabian" ]
horses.sort(reverse=True)
print(horses)

#you can maintain your original list but presented it in a sorted order with the "sorted() statement"
horses = [ "Appalosa", "Fresian", "Mustang", "Clydesdale", "Arabian" ]

print("See our original list")
print(horses)

print("\n See the new sorted list down here")
print(sorted(horses))

#you can also put a list in reverse order without being arranged in order with the ".reverse()" statement.
flowers = [ "sunflower, daisy", "tulip", "rose" ]
print(flowers)

flowers = [ "sunflower, daisy", "tulip", "rose" ]
flowers.reverse()
print(flowers)

#you can find the length of a list with the "len()" statement.
footwear = [ "sneakers", "boots", "heels", "sandals", "loafers" ]
print (len(footwear))
