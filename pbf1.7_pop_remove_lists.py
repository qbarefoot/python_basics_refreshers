#you can use the ".pop()" statement to take the last element in a list and store it in a variable.
movies = [ "The Dark Knight", "Mad-Max", "The Wild Bunch", "Pulp Fiction" ]
print(movies)

pop_movies = movies.pop()
print(movies)
print(pop_movies)

#the .pop() statement can be used in a "f-string" and can include a element index for example your favortie food. Remember a popped element is no longer stored in the list!
food = [ "pizza", "burgers", "tacos", "spaghetti", "salad" ]

favorite_food = food.pop(2)
print(f"I love eating, {favorite_food.lower()}.")

#you can use the ".remove" statement to delete an element from the list and give a reason variable wise for being removed.
destination = [ "New Orleans", "Los Angeles", "New York", "Dallas", "Seattle" ]
print(destination)

destination.remove("New Orleans")
print(destination)

new_destination = [ "Austin", "Portland", "San Francisco", "Raleigh", "Atlanta" ]
print(new_destination)

too_far = "Portland"
new_destination.remove(too_far)
print(new_destination)
print(f"\nA plane ride to {too_far.title()} is 8 hours!")