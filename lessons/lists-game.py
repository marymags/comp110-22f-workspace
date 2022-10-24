"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list() 

"""immediately enters the while loop. Now the length of rolls is not equal to zero. """
while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

# Remove an item from the list by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# sum the values of our rolls!
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i + i + 1

print(f"Total score: {sum}")



# rolls.append(randint(1,6))
# rolls.append(randint(1,6))
# rolls.append(randint(1,6))
# print(rolls)

# # Access an individual item
# print(rolls[0])
# print(rolls[1])

# # Access the length of a list (number of items) 
# print(len(rolls))

# # Acess the last item of the list in two different ways
# # way 1
# last_index: int = len(rolls) - 1
# print(rolls[last_index])
# # way 2
# print(rolls[len(rolls) - 1])

