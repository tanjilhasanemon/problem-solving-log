'''Instructions
Write a function to find the missing number in a given integer array of 1 to 100. The function takes to parameter the array and the number of elements that needs to be in array.  For example if we want to find missing number from 1 to 6 the second parameter will be 6.

Example

missing_number([1, 2, 3, 4, 6], 6) # 5'''

def missing_number(arr, n):
    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the given array
    actual_sum = sum(arr)
    
    # The missing number is the difference between expected and actual sums
    return expected_sum - actual_sum


# Example usage
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5          


#Another Way
def missing_number(arr, n):
    # Create a set of numbers from 1 to n
    expected_numbers = set(range(1, n + 1))
    
    # Remove the numbers present in the array from the expected set
    for num in arr:
        expected_numbers.discard(num)
    
    # The remaining number in the set is the missing number
    return expected_numbers.pop() if expected_numbers else None


# Example usage
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5                          


#Another Way
def missing_number(arr, n):
    # Create a boolean array to track the presence of numbers from 1 to n
    present = [False] * (n + 1)
    
    # Mark the presence of each number in the input array
    for num in arr:
        if 1 <= num <= n:
            present[num] = True
    
    # Find the missing number by checking which index is still False
    for i in range(1, n + 1):
        if not present[i]:
            return i
    
    return None  # Return None if no number is missing                  

# Example usage     
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5


#Another Way

def missing_number(arr, n):
    # Calculate the expected product of numbers from 1 to n
    expected_product = 1
    for i in range(1, n + 1):
        expected_product *= i
    
    # Calculate the actual product of the given array
    actual_product = 1
    for num in arr:
        actual_product *= num
    
    # The missing number is the division of expected product by actual product
    return expected_product // actual_product

# Example usage
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5



#Another Way
def missing_number(arr, n):
    
    expected_list = list(range(1, n + 1))
    for num in arr:
        if num in expected_list:
            expected_list.remove(num)
    return expected_list[0] if expected_list else None

# Example usage
print(missing_number([1, 2, 3, 4, 6], 6))  # Output: 5

