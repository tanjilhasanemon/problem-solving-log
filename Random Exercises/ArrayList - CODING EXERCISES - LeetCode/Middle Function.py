'''Instructions
Write a function called middle that takes a list and returns a new list that contains all 
but the first and last elements.

myList = [1, 2, 3, 4]
middle(myList)  # [2,3]'''


def middle(lst):
    # Return a new list that excludes the first and last elements
    return lst[1:-1]

# Example usage
myList = [1, 2, 3, 4]
print(middle(myList))  # Output: [2, 3]


# Another way to implement the middle function
def middle(lst):
    # Check if the list has less than 3 elements, return an empty list in that case
    if len(lst) < 3:
        return []
    
    # Return a new list that excludes the first and last elements
    return lst[1:-1]    

# Example usage
myList = [1, 2, 3, 4]
print(middle(myList))  # Output: [2, 3] 



# Another way to implement the middle function using slicing
def middle(lst):
    # Return a new list that excludes the first and last elements using slicing
    return lst[1:len(lst)-1]
# Example usage
myList = [1, 2, 3, 4]
print(middle(myList))  # Output: [2, 3]

    
    



