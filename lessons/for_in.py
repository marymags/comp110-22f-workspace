"""An example of for in syntax."""

names: list[str] = ["Maggie", "Kaki", "Ezri", "Zab"]

# Example of iterating through names using a while loop
print("while output:")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

print("for...in output")
# The following for_in_ loop is the same as the while loop
for name in names:
    print(name)

# in terminal: python -m lessons.for_in
# while output:
# Kris
# Kaki
# Ezri
# Zab
# for...in output:
# Kris
# Kaki
# Ezri
# Zab

#These two methods are equivalent, but for_in is much more efficient. 
#What's going on in memory during the for_in loop?
