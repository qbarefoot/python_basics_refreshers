#to accomplish the task of using multiple variables in strings, we made three strings, "first_name", "last_name", and "full_name". 
#we then nested our "first_name and last_name" in "full_name". Then proceded to use a "f-string" that replaces the name of a variable with its value, run it!
first_name = ("rat")
last_name = ("man")
full_name = (f"{first_name} {last_name}")
print(full_name)

#changing the case of our variables inside strings, run it!
first_name = ("big")
last_name = ("chungus")
full_name = (f"{first_name} {last_name}")
print(full_name.title())
print(full_name.lower())
print(full_name.upper())

#we used the greeting "Hows it going" in our "f-string" and called on our "full_name" variable in conjuction with combining it with .title", run it!
print(f"Hows it going, {full_name.title()}?")

#you can assign a variable as well for example "message" below in our "f-string", run it!
first_name = ("big")
last_name = ("chungus")
full_name = (f"{first_name} {last_name}")
message = (f"See you later, {full_name.upper()}!")
print(message)
