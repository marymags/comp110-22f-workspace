"""Examples of the tuple and range sequences."""

# An example of a tuple without type aliasing
goat: tuple[str, int] = ("MJ", 23)
# Tuples are sequences, so they're zero-indexed
print(goat[0])
print(goat[1])

# Sequences have lengths 
print(len(goat))

# Printing a tuple produces its literal syntax
print(goat)

# Print both items on the same line
print(f"{goat[0]} is number {goat[1]}")

# Sequences are interable with for ... in loops
# Meaning you can loop over them with for ... in loops
for item in goat:
    print(item)


# Tuples, unlike lists, are imutable (line 21 would be an error)
# Which means we cannot reassign items, or append or pop
# goat[0] = "LBJ"

# We can 'invent' our owm type with a type alias
Player = tuple[str, int]

# Once we've aliased the type, we can create variables of that type
unc_poy: Player = ("Bacot", 5)

# In a tramge world where jersey number chnages...
unc_poy = (unc_poy[0], unc_poy[1] + 1)

# A range is another common sequence type
zero_to_nine: range = range(0, 10, 1)
# the three arguments in the range constructor are start, stop, and step

# We can access items in the range
print(zero_to_nine[0])
print(zero_to_nine[0])

# We can use for... in for ranges and index them
for i in zero_to_nine:
    print(i)  # this prints each item in zer_to_nine

# We can have different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)


names: list[str] = ["Kris", "Ali", "Mic", "Lebron"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")


for i in range(0, len(names), 2): 
    print(f"{i}. {names[i]}")


print(odds_to_99.stop)


