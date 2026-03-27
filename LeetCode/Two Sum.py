'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]'''


from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[num] = i
            
            
# Example usage:
solution = Solution()               
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Output : [1, 2]
print(solution.twoSum([3, 3], 6))          # Output : [0, 1]



#Another solution using brute force approach:       
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]   
                
# Example usage:
solution = Solution()                           
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1] 
print(solution.twoSum([3, 2, 4], 6))       # Output : [1, 2]
print(solution.twoSum([3, 3], 6))          # Output : [0, 1]


# Time complexity: O(n) for the hash map solution, O(n^2) for the brute force solution.
# Space complexity: O(n) for the hash map solution, O(1) for the brute force solution.



'''The hash map solution is more efficient than the brute force solution, 
as it allows us to find the complement of each number in constant time. 
The brute force solution, on the other hand, requires us to check every pair of numbers, 
resulting in a time complexity of O(n^2).'''




#Another solution

def two_sum(nums, target):
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i

nums = [2, 7, 11, 15]
target = 9
indices = two_sum(nums, target)
print(f"Indices of the two numbers are: {indices}")





