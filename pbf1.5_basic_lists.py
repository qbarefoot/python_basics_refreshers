#making a Python list is simple all examples in it can be related or unrelated, run it!
garden = ["beans", "peppers", "tomatoes", "onions", "basil"]
print(garden)

#you can access a certain elements in a list by listing the index in the print statement "remember the index starts at "0" instead of "1", run it!
garden = ["beans", "peppers", "tomatoes", "onions", "basil"]
print(garden[0])
print(garden[3])

#in Python you can access the last element in a last by using -1, run it!
garden = ["beans", "peppers", "tomatoes", "onions", "basil"]
print(garden[-1])

#you can append a element in the list, that we learned previously, run it!
garden = ["beans", "peppers", "tomatoes", "onions", "basil"]
print(garden[3].upper())

#you can pull an element from a list to insert in to a "f-string", run it!
garden = ["beans", "peppers", "tomatoes", "onions", "basil"]
information = (f"a vegetable that is high yield is, {garden[2].upper()}!")
print(information)
