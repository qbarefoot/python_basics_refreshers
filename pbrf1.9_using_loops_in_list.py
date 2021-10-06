#we can use a "for" loop to cycle through the names of elements in a list.
guns = [ "winchester", "remington", "colt", "savage", "henry", "smith & wesson"]
for gun in guns:
    print(gun)

#you can use in a "f-string" in a "for" loop as well to print multiple messages that include all elements in a list.
guns = [ "winchester", "remington", "colt", "savage", "henry", "smith & wesson"]
for gun in guns:
    print(f"A {gun.title()}, is really expensive!")
    print(f"I will have to save up money to buy a {gun.title()}.")

print("You should take a course on safety no matter what you buy.")

#be careful when writing "for" loops as you can experience indentation errors, which the terminal will let you know.
#you can also experience logical errors, which will run the code, but due to over/under indentation can produce unwanted outcomes in loops. Such as not giving the end of a statement in your loop or not included in every element.
