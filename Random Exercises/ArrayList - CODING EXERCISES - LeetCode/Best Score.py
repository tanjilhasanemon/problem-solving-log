'''
Instructions
Given a list, write a function to get first, second best scores from the list.

List may contain duplicates.

Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87'''


def first_second(myList):
    first = second = float('-inf')
    for score in myList:
        if score > first:
            second = first
            first = score
        elif first > score > second:
            second = score
    return first, second

# Test the function with the provided example
myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(myList))  # Output should be (90, 87)


'''The function first_second iterates through the list of scores, 
updating the first and second best scores as it goes. It handles duplicates by 
only updating the second best score if the current score is strictly 
between the first and second best scores. '''


# The time complexity of this function is O(n), where n is the number of elements in the list,
# because it requires a single pass through the list to determine the first and second best scores.

#Alternative approach using built-in functions:

def first_second_alternative(myList):
    unique_scores = list(set(myList))
    unique_scores.sort(reverse=True)
    return unique_scores[0], unique_scores[1]


# Test the alternative function with the provided example
print(first_second_alternative(myList))  # Output should be (90, 87)


'''The alternative function first creates a set from the list to remove duplicates, 
then converts it back to a list and sorts it in descending order. 
Finally, it returns the first two elements of the sorted list as the first and second best scores.  
The time complexity of this alternative function is O(n log n) due to the sorting step, 
which is less efficient than the O(n) approach of the first function.'''

# Both functions will return the same result, but the first function is more efficient for larger lists.



