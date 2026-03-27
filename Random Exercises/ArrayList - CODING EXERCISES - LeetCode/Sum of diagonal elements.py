'''Instructions
Given 2D list calculate the sum of diagonal elements.

Example

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 

diagonal_sum(myList2D) # 15'''


def diagonal_sum(matrix):
    # Initialize the sum variable
    total_sum = 0
    
    # Get the number of rows in the matrix
    n = len(matrix)
    
    # Loop through the matrix and add the diagonal elements
    for i in range(n):
        total_sum += matrix[i][i]  # Add the primary diagonal element
        total_sum += matrix[i][n - 1 - i]  # Add the secondary diagonal element
    
    # If the matrix has an odd number of rows, subtract the middle element once
    if n % 2 == 1:
        total_sum -= matrix[n // 2][n // 2]
    
    return total_sum

# Example usage
myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sum(myList2D))  # Output: 25 (1 + 5 + 9 + 3 + 7)


# Another way to implement the diagonal_sum function
def diagonal_sum(matrix):   
    # Initialize the sum variable
    total_sum = 0
    
    # Get the number of rows in the matrix
    n = len(matrix)
    
    # Loop through the matrix and add the diagonal elements
    for i in range(n):
        total_sum += matrix[i][i]  # Add the primary diagonal element
    
    return total_sum    

# Example usage
myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sum(myList2D))  # Output: 15 (1 + 5 + 9)


# Another way to implement the diagonal_sum function using list comprehension
def diagonal_sum(matrix):
    # Get the number of rows in the matrix
    n = len(matrix)
    
    # Calculate the sum of the primary diagonal elements using list comprehension
    total_sum = sum(matrix[i][i] for i in range(n))
    
    return total_sum

# Example usage
myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sum(myList2D))  # Output: 15 (1 + 5 + 9) 



# Another way to implement the diagonal_sum function using a single loop
def diagonal_sum(matrix):
    # Initialize the sum variable
    total_sum = 0
    
    # Get the number of rows in the matrix
    n = len(matrix)
    
    # Loop through the matrix and add the diagonal elements
    for i in range(n):
        total_sum += matrix[i][i]  # Add the primary diagonal element
    
    return total_sum

# Example usage
myList2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sum(myList2D))  # Output: 15 (1 + 5 + 9)


