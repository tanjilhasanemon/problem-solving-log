'''Instructions
Write a function to remove the duplicate numbers on given integer array/list.

Example

remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]'''


def remove_duplicates(nums):
    unique_nums = set(nums)
    return list(unique_nums)

# Test the function with the provided example
print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))  # Output should be [1, 2, 3, 4, 5]

'''The function remove_duplicates takes a list of numbers as input, 
converts it to a set to remove duplicates, and then converts it back to a list before returning it. 
The order of the elements in the output may not be the same as the input list due to the nature of sets, 
which do not maintain order. If you want to preserve the original order 
of the first occurrence of each number, you can use the following approach:'''


# Alternative approach to preserve order

def remove_duplicates_preserve_order(nums):
    seen = set()
    unique_nums = []
    for num in nums:
        if num not in seen:
            unique_nums.append(num)
            seen.add(num)
    return unique_nums

# Test the alternative function with the provided example
print(remove_duplicates_preserve_order([1, 1, 2, 2, 3, 4, 5]))  # Output should be [1, 2, 3, 4, 5]  
'''The alternative function remove_duplicates_preserve_order iterates through the list of numbers,
keeping track of seen numbers in a set and appending unique numbers 
to a new list while preserving their original order. 
The time complexity of this function is O(n), 
where n is the number of elements in the input list.'''