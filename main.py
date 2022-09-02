# Randomisation
import random
# randint(from, to) - gives random no between from and to
randno = random.randint(0, 3)
print(randno)
# random() - gives random no between 0 to 0.99
randnos = 2 * random.random()
print(randnos)

# Lists
# creating list
fruits = ["apple", "Orange", "grapes"]
# append - adds a single item to the list
fruits.append("carrot")
# extend - adds multiple items to the list
fruits.extend(["pencil", "pen"])

# Who is going to pay the bill
names_string = input("enter the names who are willing to pay the bill and put comma before entering the new name \n")
# split("") - splits the string of words into strings and puts them into a list
names = names_string.split(", ")
# getting the length of the list
no_of_names = len(names)
print(no_of_names)
# selecting a guy randomly from the list and printing him
random_name = random.randint(0, no_of_names - 1)
print(f"{names[random_name]} is going to pay the bill")
