'''Instructions
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

DO NOT allocate another 2D matrix and do the rotation.

Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

'''


def rotate(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
    return matrix   

# Test the function with the provided example
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(matrix))  # Output should be [[7, 4, 1], [8, 5, 2], [9, 6, 3]]         

'''The function rotate first transposes the matrix by swapping elements across the diagonal, 
and then reverses each row to achieve the 90-degree clockwise rotation. 
The time complexity of this function is O(n^2), where n is the number of rows (or columns) in the matrix, 
because it requires two passes through the matrix: one for transposing and one for reversing the rows. 
The space complexity is O(1) since the rotation is done in-place without using any additional data structures.'''


# Alternative approach using list comprehension to create a new rotated matrix

def rotate_alternative(matrix):
    n = len(matrix)
    return [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)] 

# Test the alternative function with the provided example
matrix = [[1, 2, 3], [4, 5, 6 ], [7, 8, 9]]
print(rotate_alternative(matrix))  # Output should be [[7, 4, 1], [8, 5, 2], [9, 6, 3]] 


'''The alternative function rotate_alternative creates a new rotated matrix using list comprehension. 
It constructs the new matrix by iterating through the original matrix and rearranging the elements according to the rotation. 
The time complexity of this function is also O(n^2) due to the nested list comprehension, 
and the space complexity is O(n^2) because it creates a new matrix to store the rotated values.'''


# Both functions will return the same result, but the first function is more efficient in terms of space since it rotates the matrix in-place. 

# The second function is more concise and easier to read, but it uses additional space for the new matrix.

