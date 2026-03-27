'''Instructions
Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

Example

pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']


Note:

4+3 comes from second and third elements from the main list.

3+4 comes from third and seventh elements from the main list.'''


def pair_sum(nums, target):
    pairs = []
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append(f"{complement}+{num}")
        seen.add(num)
    return pairs


# Test the function with the provided example
print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))  # Output should be ['2+5', '4+3', '3+4', '-2+9']   
'''The function pair_sum iterates through the list of numbers, calculating the complement of each number with 
respect to the target sum. If the complement has already been seen, it adds the pair to the list of pairs.
The time complexity of this function is O(n), where n is the number of elements in the input list, 
because it requires a single pass through the list to find all pairs. The space complexity is also O(n) 
in the worst case, if all numbers are unique and stored in the seen set.'''



# Alternative approach using a dictionary to count occurrences of numbers
def pair_sum_alternative(nums, target):
    pairs = []
    count = {}
    for num in nums:
        complement = target - num
        if complement in count and count[complement] > 0:
            pairs.append(f"{complement}+{num}")
            count[complement] -= 1
        else:
            count[num] = count.get(num, 0) + 1
    return pairs


# Test the alternative function with the provided example
print(pair_sum_alternative([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))  # Output should be ['2+5', '4+3', '3+4', '-2+9']

'''The alternative function pair_sum_alternative uses a dictionary to count the occurrences of each number. 
It checks for the complement in the dictionary and updates the count accordingly. 
The time complexity of this function is also O(n), where n is the number of elements in the input list, 
because it requires a single pass through the list to find all pairs. 
The space complexity is O(n) in the worst case, if all numbers are unique and stored in the count dictionary.'''



