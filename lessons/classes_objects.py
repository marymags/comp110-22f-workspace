"""Example of a class and objects instantiation."""


class Pizza: 
    """Models the idea of a Pizza."""

    # Attribute Definitions
    size: str = "small"
    toppings: int = 0
    extra_cheese: bool = False

    def __init__(self, size: str, toppings: int):
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings
        
# # function
# def price(pizza: Pizza) -> float:
#     """Calculate the price of a Pizza."""
#     total: float = 0.0
#     if pizza.size == "large":
#         total += 10.0
#     else:
#         total += 8.0
#     total += pizza.toppings * 0.75
#     if pizza.extra_cheese:
#         total += 1.0
#     return total

# method
    def price(self, tax: float) -> float:
        """Pizza can calculate its own price. Capability of Pizza object."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0
        total += self.toppings * 0.75
        if self.extra_cheese:
            total += 1.0
        total *= tax
        return total



a_pizza: Pizza = Pizza()
a_pizza.size = "large"
a_pizza.toppings = 3
print(Pizza)
print(a_pizza)
print(a_pizza.size)
# Output
# <class '__main__.Pizza'>
# <__main__.Pizza object at 0x000001C466C83F40> # this big number is a memory address in our heap.
# large
# print(f"Price: ${price(a_pizza)}")
print(f"Price: ${a_pizza.price(1.05)}")
# ^ this is a method call
# we passed a reference from a_pizza into def price the parameter pizza
# previously, if you wanted to define a function to calculate the price of a pizza,
# you would have had to declare all of these variables.
# But with object-oriented programming, we're able to define
# a new idea, the idea of a piza, and every pizza
# has these three attributes bundled with it.
# the attributes can be any time, and a class can have any amount of attributes.

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True
print(a_pizza.size)
print(another_pizza.size)
print(f"Price: ${another_pizza.price(1.05)}")