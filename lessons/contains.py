""" An example of a list utility program."""

# Name: contains
# Function with 3 
# needle is the value we're searching for
# haystack is the list of values we're searching in.
# Returns type: bool

def contains(needle: str, haystack: list[str]) -> bool: 
    """searching for one specific value within list of many values"""
    i: int = 0
    #start from first index
    #loop through each idex of list
    while i < len(haystack):
    #Test if item at this index is equal to needle
        #      # Yes! Retrun Trueif haystack[i] == needle:
        return True
    #Return False
return False 