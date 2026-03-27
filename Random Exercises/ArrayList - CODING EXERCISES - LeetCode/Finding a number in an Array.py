#Check if any number in the array is equal to the given number
'''Example 1:
Input: nums = [1, 2, 3, 4, 5], target = 3
Output: True            
Example 2:
Input: nums = [1, 2, 3, 4, 5], target = 6
Output: False
Example 3:
Input: nums = [1, 2, 3, 4, 5], target = 1
Output: True'''


from ast import List    
class Solution:
    def findNumber(self, nums: List[int], target: int) -> bool:
        return target in nums
    
# Example usage:
solution = Solution()
print(solution.findNumber([1, 2, 3, 4, 5], 3))  # Output: True
print(solution.findNumber([1, 2, 3, 4, 5], 6))  # Output: False
print(solution.findNumber([1, 2, 3, 4, 5], 1))  # Output: True


# Time complexity: O(n) where n is the length of the input array.
# Space complexity: O(1) since we are not using any additional data structures.


'''The solution is efficient and straightforward, utilizing the built-in 'in' operator 
to check for the presence of the target number in the array.'''


#Another solution using a set for faster lookups:
class Solution:
    def findNumber(self, nums: List[int], target: int) -> bool:
        num_set = set(nums)
        return target in num_set
# Example usage:
solution = Solution()
print(solution.findNumber([1, 2, 3, 4, 5], 3))  # Output: True
print(solution.findNumber([1, 2, 3, 4, 5], 6))  # Output: False
print(solution.findNumber([1, 2, 3, 4, 5], 1))  # Output: True



# Time complexity: O(n) for creating the set, O(1) for lookups, overall O(n).
# Space complexity: O(n) for the set.


# The set-based solution is more efficient for larger arrays due to O(1) lookups,
# but it uses additional space compared to the first solution.


'''In conclusion, both solutions are valid for finding a number in an array, 
with the first solution being more space-efficient and the second solution offering faster lookups 
at the cost of additional space.'''

''' The choice between the two solutions depends on the specific requirements of the problem,
such as the size of the input array and whether space complexity is a concern.'''



#Another solution using binary search (assuming the array is sorted):

import numpy as np
class Solution:
    def findNumber(self, nums: List[int], target: int) -> bool:
        nums.sort()  # Ensure the array is sorted
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
    
    
# Example usage:    
solution = Solution()
print(solution.findNumber([1, 2, 3, 4, 5], 3))  # Output: True
print(solution.findNumber([1, 2, 3, 4, 5], 6))  # Output: False
print(solution.findNumber([1, 2, 3, 4, 5], 1))  # Output: True  

# Time complexity: O(n log n) for sorting, O(log n) for binary search, overall O(n log n).
# Space complexity: O(1) if we sort in place, otherwise O(n) for the sorted array.






