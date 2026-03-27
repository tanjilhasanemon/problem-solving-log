'''Find the maximum product of two integers in an array where all elements are positive.

Example

arr = [1, 7, 3, 4, 9, 5] 
max_product(arr) # Output: 63 (9*7)'''


def max_product(arr):
    if len(arr) < 2:
        return None  # Not enough elements to form a product
    
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])
    
    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]
    
    return max1 * max2



# Example usage
arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)     



# Time complexity: O(n) since we traverse the array once.
# Space complexity: O(1) since we only use a constant amount of extra space.


'''The max_product function efficiently finds the two largest integers 
in the array and returns their product. 
It handles edge cases where the array has fewer than two elements by returning None.'''

'''This solution is optimal with a time complexity of O(n) and 
a space complexity of O(1), making it suitable for large input arrays.'''



# Another solution:
def max_product(arr):
    # Initialize two variables to store the two largest numbers
    max1, max2 = 0, 0  # O(1), constant time initialization

    # Iterate through the array
    for num in arr:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment

    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication

arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)



# Time complexity: O(n) since we traverse the array once.
# Space complexity: O(1) since we only use a constant amount of extra space.


#Another solution using sorting:
def max_product(arr):
    if len(arr) < 2:
        return None  # Not enough elements to form a product
    
    arr.sort()  # O(n log n) for sorting
    return arr[-1] * arr[-2]  # O(1) for accessing the last two elements



# Example usage
arr = [1, 7, 3, 4, 9, 5]
print(max_product(arr))  # Output: 63 (9*7)     

# Time complexity: O(n log n) due to sorting.
# Space complexity: O(1) if the sorting is done in-place, otherwise O(n) for the sorted array.

'''The sorting-based solution is less efficient than the first solution 
due to the O(n log n) time complexity of sorting. However, 
it is simpler to implement and may be acceptable for small input sizes.'''

