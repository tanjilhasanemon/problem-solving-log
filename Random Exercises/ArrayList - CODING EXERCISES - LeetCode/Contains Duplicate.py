'''Instructions
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example :

Input: nums = [1,2,3,1]
Output: true
Hint: Use sets to track seen numbers. If you encounter a number that is already in the set, return true. 
If you finish checking all numbers without finding duplicates, return false.'''


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False    

# Test the function with the provided example
print(contains_duplicate([1, 2, 3, 1]))  # Output should be True    


'''The function contains_duplicate iterates through the list of numbers, 
adding each number to a set called seen. If it encounters a number that is already in the set it returns True, 
indicating that a duplicate has been found. If it finishes checking all numbers without finding duplicates, 
it returns False.
The time complexity of this function is O(n), where n is the number of elements in the input list, 
because it requires a single pass through the list to check for duplicates. 
The space complexity is O(n) in the worst case, if all numbers are unique and stored in the seen set.'''


# Alternative approach using a dictionary to count occurrences of numbers
def contains_duplicate_alternative(nums):
    count = {}
    for num in nums:
        if num in count:
            return True
        count[num] = 1
    return False    

# Test the alternative function with the provided example
print(contains_duplicate_alternative([1, 2, 3, 1]))  # Output should be True

'''The alternative function contains_duplicate_alternative uses a dictionary to count the occurrences of each number. 
It checks if a number is already in the dictionary and returns True if it is, indicating a duplicate. 
If it finishes checking all numbers without finding duplicates, it returns False.'''

# The time complexity of this alternative function is also O(n), where n is the number of elements in the input list,
# because it requires a single pass through the list to check for duplicates.   

